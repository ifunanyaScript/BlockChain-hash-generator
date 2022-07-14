# Bitcoin-hash-generator
### This is a simple python program that generates a new blockchain ___block hash___.<br>
The concept of mining bitcoin sometimes seems vague to a lot of people, but I'll try to simplify it.<br>
The blockchain from it's name is a link of several blocks of transactions, i.e There are thousands of tables of transactions<br>
like so;
| Sender      | Receiver    | Amount  |
| ----------- | ----------- |---------|
| user_id     | user_id     | $900    |
| user_id     | user_id     |$45678   |

The Bitcoin Core protocol limits each block to 1mb in size, thus, each block contains at most 4000 transactions.
These transaction tables pile up on the blockchain network, but they are only added to the actual chain of blocks (BlockChain),<br>
when there's is a valid block hash for the said transaction table. This is where bitcoin miners come in play. The end game of<br>
mining bitcoin, is to generate a new hash for the recent transaction tables. When said new hash is generated, the transaction table <br>
can now be added to the BlockChain as a valid block with the said miner having a reward of x bitcoins, depending on what year you mined it.

| Sender      | Receiver    | Amount  |
| ----------- | ----------- |---------|
| user_id     | user_id     | $900    |
| user_id     | user_id     |$45678   |
| REWARD     | ifunanyaScript     | 6.25BTC |


###### How is the hash generated?
The hash
