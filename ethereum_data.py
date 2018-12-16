import time
from web3 import Web3 

# create the ethereum data mediator
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/341dcb557aa64fdbbb22b163f2697430"))

# extract block information
def getBlocks(n_blocks):
    blocks_list = list() # list of blocks to return
    previous_block_hash  = str() # store the hash to the previous block hash
    block = None # store the block here
    for i in range(n_blocks):
        # get the latest block
        if i==0:
            block = web3.eth.getBlock('latest')
            time.sleep(2) # we are sleeping the process for 2 
                          #seconds because the api is async. 
                          #This needs to be improved in coming implementations
        else:
            block = web3.eth.getBlock(previous)
            time.sleep(2)
        blocks_list.append(block)
        previous = block.hash.hex()
    return blocks_list