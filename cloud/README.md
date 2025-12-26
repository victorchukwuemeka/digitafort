# Solana RPC Node on Microsoft Azure - Project README

**Project Goal**: Deploy a production-grade, secure, and monitored Solana RPC node on Microsoft Azure.  
This project will teach you Azure from beginner to advanced level while building something directly useful for your Web3/Solana development work.

**Why this project?**  
- Covers ~90% of core Azure topics (VMs, Networking, Security, Storage, Monitoring, Cost Management, IaC).  
- Gives you a reliable custom RPC endpoint (better latency/control than public providers).  
- Portfolio piece you can showcase on GitHub/X.  
- Directly leverages your existing Solana + Rust knowledge.

**Estimated Time**: 1–3 weeks (2–4 hours/day)

## Prerequisites

1. **Microsoft Azure Account**  
   - Sign up at https://azure.microsoft.com/free/ (free tier + $200 credit for 30 days).  
   - Complete AZ-900 Fundamentals on Microsoft Learn (optional but recommended — ~8 hours, free sandboxes).

2. **Basic Tools Installed Locally**  
   - Azure CLI (`az`) — install: https://learn.microsoft.com/cli/azure/install-azure-cli  
   - SSH client (built-in on macOS/Linux, OpenSSH on Windows)  
   - Solana CLI (you probably already have this)  
   - Git (optional, for version control)

3. **Knowledge**  
   - Basic Solana validator/RPC setup (you already know this).

## Project Phases & Steps

### Phase 1: Azure Basics & First VM (Day 1–2)

Goal: Get comfortable with the portal and deploy a simple Linux VM.

1. Log into the Azure Portal: https://portal.azure.com
2. Create a **Resource Group** (e.g., `solana-rpc-rg`) — logical container for all resources.
3. Create a **Linux Virtual Machine**:
   - OS: Ubuntu Server 22.04 LTS
   - Size: Start small for testing (e.g., Standard_B2s or B4ms — cheap)
   - Authentication: SSH public key (generate if needed)
   - Open ports: 22 (SSH), temporarily 8899 (RPC) for testing
4. Connect via SSH: `ssh username@public-ip`
5. Install Solana CLI on the VM and run a quick test (e.g., `solana balance --url https://api.mainnet-beta.solana.com`)

**Topics Learned**: Resource groups, VMs, basic networking (public IP, NSGs), SSH access.

### Phase 2: Production-Grade RPC Node (Day 3–7)

Goal: Upgrade to a real RPC-capable machine.

1. **Choose Proper VM Size** (critical for performance)  
   Recommended for full RPC node (2025 specs):  
   - `Standard_D16s_v5` or `Standard_E16-8s_v5` (16 vCPU, 64–128 GB RAM)  
   - Or NVMe-optimized: `Standard_L8s_v3` (better disk I/O)  
   (Start smaller and resize later if budget tight)

2. **Storage**  
   - Add premium SSD or ultra disk (minimum 2–4 TB for ledger)  
   - Attach as data disk and format/mount.

3. **Install & Configure Solana RPC Node**  
   Follow official docs: https://docs.solana.com/operations/setup-an-rpc-node

   Key commands on the VM:
   ```bash
   sh -c "$(curl -sSfL https://release.solana.com/stable/install)"
   export PATH="$HOME/.local/share/solana/install/active_release/bin:$PATH"

   # Start as non-voting RPC node
   solana-validator \
     --identity identity.json \
     --vote-account vote-account.json \
     --no-voting \
     --full-rpc-api \
     --rpc-port 8899 \
     --private-rpc \
     --enable-rpc-transaction-history \
     --limit-ledger-size
   ```

4. Use systemd to run as service (for auto-restart).

**Topics Learned**: Compute sizing, managed disks, performance optimization.

### Phase 3: Networking & Security Hardening (Day 8–10)

1. Create a **Virtual Network (VNet)** and subnet.
2. Move VM into the VNet.
3. Configure **Network Security Group (NSG)**:
   - Allow inbound: SSH (only from your IP), RPC port 8899 (restrict to trusted IPs or use private endpoint later)
   - Allow gossip/repair ports if needed
4. Optional: Set up **Azure Bastion** for secure SSH (no public exposure).

**Topics Learned**: VNets, NSGs, secure access — the “hardest” Azure part.

### Phase 4: Monitoring, Alerts & Cost Control (Day 11–12)

1. Enable **Azure Monitor** → Metrics for CPU, disk, network.
2. Set up **alerts** (email/SMS) for high CPU or disk full.
3. Use **Cost Management** → Set budget alerts.
4. Enable **diagnostic settings** → Log to storage account.

**Topics Learned**: Observability, proactive ops.

### Phase 5: Infrastructure as Code (IaC) – Automation (Day 13+)

1. Learn **Bicep** (Azure-native) or **Terraform**.
2. Write a script to deploy the entire setup (VM, disks, NSG, monitoring) in one command.
   - Azure quickstart templates: https://github.com/Azure/azure-quickstart-templates
   - Search GitHub for “azure solana terraform” examples.

**Topics Learned**: Reproducible, version-controlled infrastructure.

### Bonus Extensions (When Comfortable)

- Containerize the node with Docker → Deploy on **Azure Kubernetes Service (AKS)**.
- Add **Azure Blob Storage** for ledger snapshots/backups.
- Front with **Azure Application Gateway** or **Load Balancer**.
- Integrate **Azure Functions** for off-chain relayers.

## Tracking Progress

Create a GitHub repo: `solana-azure-rpc-node`  
Include:
- Screenshots of portal setup
- Bicep/Terraform files
- Scripts and config notes
- README.md (this file!)

## Resources

- Microsoft Learn AZ-900: https://learn.microsoft.com/training/paths/azure-fundamentals/
- Solana RPC Guide: https://docs.solana.com/operations/setup-an-rpc-node
- Azure VM Docs: https://learn.microsoft.com/azure/virtual-machines/
- YouTube: Search “Deploy Solana Node on Azure” (2024 tutorials still valid)

You now have a complete, step-by-step roadmap. Follow it sequentially — each phase builds on the previous.  
Once finished, you’ll have deep Azure knowledge **and** your own high-performance RPC endpoint.

Good luck — ping me when you hit a snag or finish Phase 2! You've got this. 🚀