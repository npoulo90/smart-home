import os
import sys

def check_directory_structure():
    # Define expected directories and files
    expected_structure = {
        'services': {
            'api-gateway': ['Dockerfile', 'requirements.txt', 'app'],
            'smart-home': ['Dockerfile', 'requirements.txt', 'app'],
            'kroger-api': ['app'],
        },
        'infra': {
            'traefik': ['certs'],
            'vault': ['policies', 'vault.hcl'],
            'homeassistant': ['automations.yaml', 'configuration.yaml', 'secrets.yaml'],
        }
    }

    # Check services directory
    for service, files in expected_structure['services'].items():
        service_path = os.path.join('services', service)
        if not os.path.exists(service_path):
            print(f"Missing service directory: {service_path}")
            continue
        
        for file in files:
            file_path = os.path.join(service_path, file)
            if not os.path.exists(file_path):
                print(f"Missing file: {file_path}")

    # Check infra directory
    for infra, files in expected_structure['infra'].items():
        infra_path = os.path.join('infra', infra)
        if not os.path.exists(infra_path):
            print(f"Missing infra directory: {infra_path}")
            continue
        
        for file in files:
            file_path = os.path.join(infra_path, file)
            if not os.path.exists(file_path):
                print(f"Missing file: {file_path}")

    print("Directory structure check completed.")

if __name__ == "__main__":
    check_directory_structure()
    sys.exit(0)
