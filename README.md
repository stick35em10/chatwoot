# Deploy Chatwoot on Render

This directory contains a `render.yaml` file to deploy Chatwoot on Render.

## Steps to Deploy

1.  **Fork the Chatwoot Repository:**
    -   Go to the official Chatwoot GitHub repository: [https://github.com/chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)
    -   Click the "Fork" button to create a copy of the repository under your GitHub account.

2.  **Update the `render.yaml` file:**
    -   Open the `render.yaml` file in this directory.
    -   Replace `https://github.com/YOUR_USERNAME/chatwoot` with the URL of your forked Chatwoot repository.

3.  **Deploy on Render:**
    -   Go to your Render dashboard.
    -   Click "New" -> "Blueprint".
    -   Connect your GitHub account and select your forked Chatwoot repository.
    -   Render will detect the `render.yaml` file and propose to create the services.
    -   Review and confirm the deployment.

4.  **Configure Environment Variables:**
    -   After the initial deployment, you will need to configure additional environment variables in the Render dashboard for the `chatwoot-web` and `chatwoot-worker` services.
    -   Refer to the `.env.example` file in the Chatwoot repository for a full list of required environment variables, especially for mailer and storage settings.
