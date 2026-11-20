# Role-Based Voting Smart Contract with Voter Authorization using Solidity on Remix IDE

A Solidity smart contract for a controlled voting system. An **owner** registers candidates, authorizes eligible voters and closes the election. Only **authorized addresses** can vote, and each can vote **once**. The contract was compiled, deployed and tested in Remix IDE on the Remix VM (Cancun).

![Solidity](https://img.shields.io/badge/Solidity-%5E0.8.0-363636?logo=solidity)
![Remix IDE](https://img.shields.io/badge/Tested%20on-Remix%20IDE-blue)
![EVM](https://img.shields.io/badge/Remix%20VM-Cancun-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Table of Contents
- [Objective](#objective)
- [Key Features](#key-features)
- [Contract Design](#contract-design)
- [Access Control Matrix](#access-control-matrix)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Execution Steps and Results](#execution-steps-and-results)
- [Output Table](#output-table)
- [Screenshots](#screenshots)
- [Limitations and Future Work](#limitations-and-future-work)

---

## Objective
- Restrict administrative actions to the contract owner
- Allow only authorized addresses to vote
- Enforce one vote per voter
- Support a controlled voting period (open and close)
- Expose vote counts through a read-only function

## Key Features
- **Owner-only administration**: the `onlyOwner` modifier protects `addCandidate`, `authorizeVoter` and `endVoting`
- **Voter whitelist**: `authorizedVoters` mapping blocks unregistered addresses
- **Double-vote prevention**: `hasVoted` mapping
- **Voting window control**: the `isActive` modifier rejects votes after `endVoting()`
- **ID validation**: candidate IDs start at 1 and must be within range
- **Transparent tally**: any address can read vote counts

## Contract Design

### State Variables
| Variable | Type | Purpose |
|---|---|---|
| `owner` | `address` | Deployer of the contract, holds admin rights |
| `votingActive` | `bool` | `true` while voting is open |
| `candidateCount` | `uint` | Number of registered candidates (also used as ID) |
| `candidates` | `mapping(uint => Candidate)` | Candidate records by ID |
| `authorizedVoters` | `mapping(address => bool)` | Whitelist of eligible voters |
| `hasVoted` | `mapping(address => bool)` | Tracks addresses that already voted |

### Struct
```solidity
struct Candidate {
    uint id;
    string name;
    uint voteCount;
}
```

### Modifiers
| Modifier | Condition | Revert Message |
|---|---|---|
| `onlyOwner` | `msg.sender == owner` | `Not owner` |
| `isActive` | `votingActive == true` | `Voting is not active` |

### Functions
| Function | Access | Description |
|---|---|---|
| `constructor()` | - | Sets the deployer as owner and opens voting |
| `addCandidate(string)` | Owner | Registers a new candidate with the next ID |
| `authorizeVoter(address)` | Owner | Adds an address to the voter whitelist |
| `vote(uint)` | Authorized voter, voting active | Casts one vote for the given candidate ID |
| `getVotes(uint)` | Public view | Returns the vote count of a candidate |
| `endVoting()` | Owner | Closes the election |

### Validation in `vote()`
```solidity
require(authorizedVoters[msg.sender], "Not authorized");
require(!hasVoted[msg.sender], "Already voted");
require(_candidateId > 0 && _candidateId <= candidateCount, "Invalid ID");
```

## Access Control Matrix
| Action | Owner | Authorized Voter | Unauthorized Address |
|---|---|---|---|
| Add candidate | Yes | No | No |
| Authorize voter | Yes | No | No |
| Vote (once) | Only if authorized | Yes | No |
| View votes | Yes | Yes | Yes |
| End voting | Yes | No | No |

## Project Structure
```
07-role-based-voting-solidity-remix/
├── contracts/
│   └── Voting.sol
├── screenshots/
│   ├── 01_compile_success.png
│   ├── 02_deploy_success.png
│   ├── 03_add_candidates.png
│   ├── 04_authorize_voter.png
│   ├── 05_cast_vote.png
│   ├── 06_view_results.png
│   └── 07_end_voting.png
├── docs/
│   └── blockchain7.docx
└── README.md
```

## Getting Started

### Prerequisites
- A web browser
- [Remix IDE](https://remix.ethereum.org) (no installation required)

### Setup
1. Create `Voting.sol` in Remix and paste the code from `contracts/Voting.sol`.
2. Open the **Solidity Compiler** tab and click **Compile Voting.sol**.
3. Open **Deploy & Run Transactions**, select **Remix VM (Cancun)** and click **Deploy**.

## Execution Steps and Results

| Step | Action | Details | Expected Result |
|---|---|---|---|
| 1 | Compile | Solidity Compiler tab, compile `Voting.sol` | Compilation successful |
| 2 | Deploy | Remix VM (Cancun), click Deploy | Contract deployed, deployer becomes owner |
| 3 | Add candidates | `addCandidate("Alice")`, `("Bob")`, `("Charlie")` | 3 successful transactions, `candidateCount = 3` |
| 4 | Authorize voter | Paste a voter address into `authorizeVoter()` | Address is whitelisted |
| 5 | Cast vote | Switch to the authorized account, call `vote(1)` | Vote recorded for Alice |
| 6 | View results | `getVotes(1)` | Returns `1` |
| 7 | End voting | Switch back to the owner, call `endVoting()` | `votingActive = false` |

## Output Table
| Candidate ID | Name | Votes |
|---|---|---|
| 1 | Alice | 1 |
| 2 | Bob | 0 |
| 3 | Charlie | 0 |

## Screenshots
| Step | Preview |
|---|---|
| 1. Compile success | ![Compile](screenshots/01_compile_success.png) |
| 2. Deploy success | ![Deploy](screenshots/02_deploy_success.png) |
| 3. Add candidates | ![Candidates](screenshots/03_add_candidates.png) |
| 4. Authorize voter | ![Authorize](screenshots/04_authorize_voter.png) |
| 5. Cast vote | ![Vote](screenshots/05_cast_vote.png) |
| 6. View results | ![Results](screenshots/06_view_results.png) |
| 7. End voting | ![End](screenshots/07_end_voting.png) |

## Limitations and Future Work
- `endVoting()` is permanent, and there is no function to reopen or restart an election.
- Authorization cannot be revoked once granted.
- The same candidate name can be added more than once.
- No events are emitted, which makes off-chain tracking harder.
- Possible improvements:
  - Add events such as `Voted`, `VoterAuthorized` and `VotingEnded`
  - Add `revokeVoter()` and a `getWinner()` function
  - Add a voting deadline using `block.timestamp`
  - Allow batch voter authorization
  - Build a front end using Ethers.js or Web3.js

## Comparison with Exercise 5
| Feature | Exercise 5 | Exercise 7 |
|---|---|---|
| Candidates | Hard-coded in constructor | Added dynamically by owner |
| Voter eligibility | Any address | Only authorized addresses |
| Admin role | None | Owner with `onlyOwner` |
| Voting period | Always open | Can be closed with `endVoting()` |
| Storage | Array | Mapping by ID |

## Tech Stack
Solidity `^0.8.0` | Remix IDE | Remix VM (Cancun)

## License
This project is licensed under the MIT License.
