// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VotingSystem {

    struct Candidate {
        string name;
        uint voteCount;
    }

    Candidate[] public candidates;
    mapping(address => bool) public hasVoted;

    constructor() {
        candidates.push(Candidate("Alice", 0));
        candidates.push(Candidate("Bob", 0));
        candidates.push(Candidate("Charlie", 0));
    }

    function vote(uint candidateIndex) public {
        require(!hasVoted[msg.sender], "You have already voted!");
        require(candidateIndex < candidates.length, "Invalid candidate");

        hasVoted[msg.sender] = true;
        candidates[candidateIndex].voteCount++;
    }

    function getCandidatesCount() public view returns (uint) {
        return candidates.length;
    }

    function getCandidate(uint index) public view returns (string memory, uint) {
        return (candidates[index].name, candidates[index].voteCount);
    }
}
