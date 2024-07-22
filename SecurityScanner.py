import sys
import os
import argparse
import json
import logging

from logger.initLogger import initLoggers
from logger.initLogger import changeDefaultLogLevel

from SASTScanner.SASTScanner import SASTScanner





# optional skript to load and set environment variables
import platform
import dotenv
if platform.system() == "Windows":
    dotenv.load_dotenv(".env")

from DependencyScanner.DependencyScanner import DependencyScanner

class SecurityScanner(object):
    """
    Main class that initilizes and starts the security scans
    :type args: argparse.Namespace - the arguments that get entered on the command line
    """
    def __init__(self, args: argparse.Namespace) -> None:
        self.path                       = args.path
        self.enableDependenyScanner     = not args.disableDependenyScanner
        self.enableInjectionScanner     = not args.disableInjectionScanner
        self.enableSecretScanner        = not args.disableSecretScanner
        self.enableCustomScanner        = args.enableCustomScanner
        self.requirementsFile           = args.requirementsFile
        self.configFile                 = args.configFile or "./securityScannerConfig.json"
        self.logLevel                   = args.logLevel
        self.logDir                     = args.logDir
        self.scanners                    = []
        initLoggers(self.logDir)
        changeDefaultLogLevel(self.logLevel)
        logging.info("SecurityScanner " + json.dumps(self.__dict__, indent=2))



        self.readConfig()

        if self.enableDependenyScanner:
            self.DependenyScanner   = DependencyScanner(self.path, self.requirementsFile, self.config.get("dependencyScanner", {}).get("db"),  self.config.get("dependencyScanner", {}).get("vulnerabilityFilter"))
            self.scanners.append(self.DependenyScanner)


        if self.enableInjectionScanner:
            self.InjectionScanner  = SASTScanner("InjectionScanner", self.path, self.config.get("injectionsScanner", []))
            self.scanners.append(self.InjectionScanner)

        if self.enableSecretScanner:
            self.SecretDetectionScanner     = SASTScanner("SecretDetectionScanner", self.path, self.config.get("secretDetectionScanner", []))
            self.scanners.append(self.SecretDetectionScanner)
        
        if self.enableCustomScanner:
            for key, value in self.config.items():
                if key in ["dependencyScanner", "injectionsScanner", "secretDetectionScanner"]: continue
                scanner = SASTScanner(key, self.path, value or [])
                self.scanners.append(scanner)


    def getVulnerabilities(self) -> list:
        vulnerabilities = []
        for scanner in self.scanners:
            vulnerabilities += scanner.vulnerarbilities
        return vulnerabilities


    def readConfig(self) -> None:
        """
        method to read and parse the configFile of the security scanner
        """
        if self.configFile and not os.path.exists(self.configFile):
            raise Exception(f"ConfigFile for SecurityScanner dont exists - please create File {self.configFile}")
        try:
            with open(self.configFile) as configFile:
                self.config = json.load(configFile)
        except Exception as e:
            logging.warn(e, exc_info=True)
            raise Exception(f"Error while parsing config - please correct JSON of {self.configFile}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Security Scanner by Malte Schadow',
        description='Scans a Python Project for Security Vulnerabilities',
        epilog='For more help please contact me'
    )

    parser.add_argument(
        '-p', '--path',
        type=str,
        default=".",  # Optional project path argument with default value
        help='Specify the path to the Python project to scan. Defaults to current directory.'
    )

    parser.add_argument(
        '-c', '--configFile',
        type=str,
        help='Path to the configFile to configurate the Security Scanner (default="securityScannerConfig.json").'
    )

    parser.add_argument(
        '-d', '--disableDependenyScanner',
        action='store_true',
        default=False,
        help="Disables the Dependency Scanner (default: enabled)"
    )

    parser.add_argument(
        '-i', '--disableInjectionScanner',
        action='store_true',
        default=False,
        help="Disables the Injection Scanner (default: enabled)"
    )

    parser.add_argument(
        '-e', '--enableCustomScanner',
        action='store_true',
        default=False,
        help="Enables the Custom Scanner - Feature demonstrates how to extend the security part (default: disabled)"
    )

    parser.add_argument(
        '-s', '--disableSecretScanner',
        action='store_true',
        default=False,
        help="Disables the Secret Scanner (default: enabled)"
    )

    parser.add_argument(
        '-r', '--requirementsFile',
        type=str,
        default="requirements.txt",
        help='Path to the requirements.txt file containing project dependencies (optional, default="requirements.txt").'
    )

    parser.add_argument(
        '-l', '--logLevel',
        type=str,
        default="INFO",
        help='Define the Loglevel (default="INFO")'
    )

    parser.add_argument(
        '-v', '--logDir',
        type=str,
        default="./logs",
        help='Directory where the logs get written (optional, default="./logs").'
    )

    args = parser.parse_args()
    logging.info(args)
    security_scanner = SecurityScanner(args)
