# Ethereum Transaction Simulation using Ganache and MetaMask

A personal Ethereum blockchain is created with Ganache, MetaMask is connected to it through a custom RPC network, and a 1 ETH transfer is executed and verified on both the wallet and the blockchain.

![Ganache](https://img.shields.io/badge/Ganache-Quickstart-E4A663)
![MetaMask](https://img.shields.io/badge/Wallet-MetaMask-F6851B?logo=metamask&logoColor=white)
![Chain ID](https://img.shields.io/badge/Chain%20ID-1337-blue)

---

## Table of Contents
- [Objective](#objective)
- [Architecture](#architecture)
- [Tools Used](#tools-used)
- [Network Configuration](#network-configuration)
- [Procedure](#procedure)
- [Transaction Analysis](#transaction-analysis)
- [Balance Verification](#balance-verification)
- [Screenshots](#screenshots)
- [Observations](#observations)
- [Security Notes](#security-notes)
- [Conclusion](#conclusion)

---

## Objective
- Deploy a local Ethereum test network using Ganache
- Connect MetaMask to the node through a custom RPC endpoint
- Import a funded Ganache account into MetaMask
- Execute and verify a native ETH transfer

## Architecture
```
 ┌───────────────┐   JSON-RPC (HTTP)   ┌────────────────────────┐
 │   MetaMask    │ ──────────────────► │   Ganache Local Node   │
 │ (Wallet / UI) │  127.0.0.1:7545     │ (Simulated EVM chain)  │
 └───────────────┘ ◄────────────────── └────────────────────────┘
   Signs and sends tx                    Mines block, updates state
```

## Tools Used
| Tool | Purpose |
|---|---|
| Ganache (Quickstart Ethereum) | Local blockchain with pre-funded test accounts (100 ETH each) |
| MetaMask | Browser wallet to sign and broadcast transactions |

## Network Configuration

**Ganache node**
| Parameter | Value |
|---|---|
| RPC Server | `http://127.0.0.1:7545` |
| Network ID | `5777` |
| Hardfork | Merge |
| Gas Limit | `6721975` |
| Gas Price | `20000000000` wei (20 Gwei) |
| Mining | Automining |

**MetaMask custom network**
| Parameter | Value |
|---|---|
| Network Name | Localhost 8545 |
| RPC URL | `http://127.0.0.1:7545` |
| Chain ID | `1337` |
| Currency Symbol | `ETH` |

> Network ID (`5777`) and Chain ID (`1337`) are separate identifiers in Ganache, so this difference is expected.

## Procedure
1. Launch Ganache and start a **Quickstart Ethereum** workspace.
2. In MetaMask, open **Settings → Networks → Add network** and enter the configuration above.
3. Copy a Ganache account's private key (key icon) and use **Import account** in MetaMask.
4. Send **1 ETH** from the imported account to another Ganache address.
5. Review the network fee and click **Confirm**.
6. Check the status in MetaMask, then verify balances and the block in Ganache.

## Transaction Analysis
| Field | Value |
|---|---|
| Status | Confirmed |
| From | `0xBd7197448E01A4d52B1ECA7b7B93718e63d5cB3b` |
| To | `0x81D0D0e08c6aDa7CaaB95c10917d0eD804767d17` |
| Amount | 1 ETH |
| Nonce | 0 |
| Gas Limit / Used | 21000 / 21000 |
| Base Fee | 0.875 Gwei |
| Priority Fee | 19.125 Gwei |
| Total Gas Fee | 0.00042 ETH |

**Fee calculation:** `21000 gas × 20 Gwei = 0.00042 ETH`

21000 gas is the fixed cost of a simple ETH transfer between externally owned accounts.

## Balance Verification
| Account | Before | After | Change |
|---|---|---|---|
| Sender (Index 0) | 100 ETH | 99 ETH (rounded) | -1 ETH and gas fee |
| Receiver (Index 1) | 100 ETH | 101 ETH | +1 ETH |
| Account (Index 2) | 100 ETH | 100 ETH | No change |

Ganache shows the current block moving from `0` to `1` and the sender's transaction count becoming `1`, which confirms the transaction was mined.

## Screenshots
| Step | Preview |
|---|---|
| Ganache Quickstart | ![Ganache](screenshots/01_ganache_quickstart.png) |
| MetaMask network setup | ![Network](screenshots/02_metamask_network_config.png) |
| Import Ganache account | ![Import](screenshots/03_import_ganache_account.png) |
| Initiate transaction | ![Initiate](screenshots/04_initiate_transaction.png) |
| Transaction confirmation | ![Confirmed](screenshots/05_transaction_notification.png) |
| Ganache verification | ![Verify](screenshots/06_ganache_verification.png) |

## Observations
- Ganache automines, so each transaction is included in a new block immediately.
- The sender paid the transfer amount plus the gas fee.
- The receiver's balance increased by exactly the transferred amount.
- Test ETH has no real value, so MetaMask's dollar amounts are not meaningful.

## Security Notes
- All keys and mnemonics here belong to a local test network and hold no real funds.
- Never import a real wallet's private key or seed phrase into a test environment.
- Never reuse a Ganache mnemonic on Ethereum mainnet.

## Conclusion
A local Ethereum network was set up with Ganache, MetaMask was connected through a custom RPC, and a 1 ETH transfer was executed and verified. This setup is the base for deploying and testing smart contracts locally before using a public testnet.
