// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FinancialTransactions {
    struct Transaction {
        uint id;
        address sender;
        address receiver;
        uint amount;
        string transactionType;
        bool isFraud;
    }

    Transaction[] public transactions;

    event TransactionRecorded(uint id, address sender, address receiver, uint amount, bool isFraud);

    function addTransaction(uint _id, address _sender, address _receiver, uint _amount, string memory _transactionType, bool _isFraud) public {
        transactions.push(Transaction(_id, _sender, _receiver, _amount, _transactionType, _isFraud));
        emit TransactionRecorded(_id, _sender, _receiver, _amount, _isFraud);
    }
}
