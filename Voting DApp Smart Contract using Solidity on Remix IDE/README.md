# Voting DApp Smart Contract using Solidity on Remix IDE

A Solidity smart contract that implements a transparent, tamper-resistant voting system on the Ethereum Virtual Machine. Each Ethereum address can cast exactly one vote. The contract was compiled, deployed and tested in Remix IDE on the Remix VM (London).

![Solidity](https://img.shields.io/badge/Solidity-%5E0.8.0-363636?logo=solidity)
![Remix IDE](https://img.shields.io/badge/Tested%20on-Remix%20IDE-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Table of Contents
- [Objective](#objective)
- [Key Features](#key-features)
- [Contract Design](#contract-design)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Test Cases and Results](#test-cases-and-results)
- [Screenshots](#screenshots)
- [Limitations and Future Work](#limitations-and-future-work)

---

## Objective
To design and deploy a smart contract that:
- Stores a list of candidates on the blockchain
- Allows each address to vote only once
- Rejects invalid votes through on-chain validation
- Exposes read-only functions to query results transparently

## Key Features
- **One address, one vote**: enforced with a `mapping(address => bool)`
- **Input validation**: invalid candidate indices revert the transaction
- **Transparent results**: anyone can read vote counts through public view functions
- **Immutable records**: votes cannot be altered once the transaction is mined
- **Free reads**: view functions cost no gas when called externally

## Contract Design

### Data Structures
| Element | Type | Purpose |
|---|---|---|
| `Candidate` | `struct { string name; uint voteCount; }` | Holds a candidate's name and vote tally |
| `candidates` | `Candidate[]` (public) | Dynamic array of all candidates |
| `hasVoted` | `mapping(address => bool)` (public) | Tracks which addresses have already voted |

### Functions
| Function | Visibility | Description |
|---|---|---|
| `constructor()` | - | Initializes three candidates (Alice, Bob, Charlie) with 0 votes |
| `vote(uint candidateIndex)` | `public` | Records a vote for the candidate at the given index |
| `getCandidatesCount()` | `public view` | Returns the total number of candidates |
| `getCandidate(uint index)` | `public view` | Returns the candidate's name and vote count |

### Validation Logic
```solidity
require(!hasVoted[msg.sender], "You have already voted!");
require(candidateIndex < candidates.length, "Invalid candidate");
```
Violating either condition reverts the transaction and restores the previous state.

## Project Structure
```
05-voting-dapp-solidity-remix/
├── contracts/
│   └── VotingSystem.sol
├── screenshots/
│   ├── 01_compile_and_deploy.png
│   ├── 02_deployed_contract.png
│   ├── 03_check_candidates_count.png
│   ├── 04_view_candidate_details.png
│   ├── 05_cast_vote.png
│   └── 06_test_voting_restriction.png
├── docs/
│   └── block_ex_05.pdf
└── README.md
```

## Getting Started

### Prerequisites
- A web browser
- [Remix IDE](https://remix.ethereum.org) (no installation required)

### Steps
1. Open Remix IDE and create a new file named `VotingSystem.sol`.
2. Paste the code from `contracts/VotingSystem.sol`.
3. Open the **Solidity Compiler** tab, select version `0.8.x` and click **Compile**.
4. Open **Deploy & Run Transactions** and set the environment to **Remix VM (London)**.
5. Click **Deploy**.
6. Interact with the deployed contract using the function buttons.

## Test Cases and Results

| # | Test | Input | Expected Result | Outcome |
|---|---|---|---|---|
| 1 | Check candidate count | `getCandidatesCount()` | Returns `3` | Pass |
| 2 | View candidate 0 | `getCandidate(0)` | `"Alice", 0` | Pass |
| 3 | View candidate 1 | `getCandidate(1)` | `"Bob", 0` | Pass |
| 4 | Cast a valid vote | `vote(0)` | Transaction mined, status 1 | Pass |
| 5 | Double voting | `vote(0)` from same account | Reverts: `You have already voted!` | Pass |

## Screenshots

| Step | Preview |
|---|---|
| Compile and deploy | ![Deploy](screenshots/01_compile_and_deploy.png) |
| Deployed contract | ![Contract](screenshots/02_deployed_contract.png) |
| Candidate count | ![Count](screenshots/03_check_candidates_count.png) |
| Candidate details | ![Details](screenshots/04_view_candidate_details.png) |
| Cast a vote | ![Vote](screenshots/05_cast_vote.png) |
| Voting restriction | ![Restriction](screenshots/06_test_voting_restriction.png) |

## Limitations and Future Work
- Any address can vote, so there is no voter registration or authentication.
- Candidates are hard-coded in the constructor.
- There is no voting deadline and no admin or owner role.
- Possible improvements:
  - Add an `owner` and `onlyOwner` modifier to manage candidates
  - Add voting start and end times
  - Emit a `Voted` event for off-chain tracking
  - Add a `getWinner()` function
  - Build a web front end using Web3.js or Ethers.js

## Tech Stack
Solidity `^0.8.0` | Remix IDE | Remix VM (London)
