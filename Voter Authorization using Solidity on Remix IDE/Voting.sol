pragma solidity ^0.8.0;
contract Voting {
    address public owner;
    bool public votingActive;
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }
    mapping(uint => Candidate) public candidates;
    mapping(address => bool) public authorizedVoters;
    mapping(address => bool) public hasVoted;
    uint public candidateCount;
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }
    modifier isActive() {
        require(votingActive, "Voting is not active");
        _;
    }
    constructor() {
        owner = msg.sender;
        votingActive = true;
    }
    function addCandidate(string memory _name) public onlyOwner {
        candidateCount++;
        candidates[candidateCount] = Candidate(candidateCount, _name, 0);
    }
    function authorizeVoter(address _voter) public onlyOwner {
        authorizedVoters[_voter] = true;
    }
    function vote(uint _candidateId) public isActive {
        require(authorizedVoters[msg.sender], "Not authorized");
        require(!hasVoted[msg.sender], "Already voted");
        require(_candidateId > 0 && _candidateId <= candidateCount, "Invalid ID");
        hasVoted[msg.sender] = true;
        candidates[_candidateId].voteCount++;
    }
    function getVotes(uint _candidateId) public view returns (uint) {
        return candidates[_candidateId].voteCount;
    }
    function endVoting() public onlyOwner {
        votingActive = false;
    }
}

