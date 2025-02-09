# Smart Home Project

## Project Structure
```
├── infra/ # Infrastructure configurations
│   ├── traefik/ # Reverse proxy setup
│   └── vault/ # Secrets management
├── services/ # Core application services
│   ├── api-gateway/ # Central control API
│   ├── kroger-api/ # Grocery API integration
│   └── smart-home/ # Home automation configs
├── scripts/ # Deployment/maintenance scripts
├── docker-compose.yml # Main compose file
└── Makefile # Development shortcuts
```

## Quick Start

To deploy the services, use the following command:

```bash
make deploy
```

### Available Commands:
- **start**: Start all services in detached mode.
  ```bash
  make start
  ```
- **stop**: Stop all running services.
  ```bash
  make stop
  ```

### Features:
1. Creates the complete directory structure
2. Sets up basic Docker Compose configuration
3. Creates starter FastAPI application with security
4. Generates essential .gitignore rules
5. Includes a Makefile for common commands
6. Adds sample Dockerfiles and requirements.txt
7. Creates a basic README with project overview

To use the script:
1. Save it as `setup_project.sh`
2. Make it executable: `chmod +x setup_project.sh`
3. Run it: `./setup_project.sh`

After running, you'll have:
- A secure foundation with Traefik and Vault
- API Gateway ready for extension
- Basic networking configuration
- Sensible defaults for development

You can then gradually add functionality to each service while maintaining the secure foundation.

### Security Considerations
- The Vault service is configured for development with a root token. Ensure to change this for production use.
