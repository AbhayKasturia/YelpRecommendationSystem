# YelpRecommendationSystem
# Steps to Run different method**

# Neural Collaborative Filtering
   - Pre-requisite (Python 2.7, h5py, theano version: '0.8.0', keras version: '1.0.7'). 
   
   - Run neural_collaborative_filtering/data_preprocessor.py (cmd: python data_preprocessor.py) to generate training and test 
     data in ./Data. Data from previous run is already available. 
     
   - Run below command to train the model and save it in neural_collaborative_filtering/Pretrain.
      ```
      python MLP.py --dataset yelp --epochs 20 --batch_size 256 --layers [64,32,16,8] --reg_layers [0,0,0,0] --num_neg 4
      --lr 0.001 --learner adam --verbose 1 --out 1
      ```
      
   - Final evaluated model is already saved in neural_collaborative_filtering/Pretrain.
   
   - Log from last run (takes approximately 4 hours to run on google cloud).
      ```
      Using Theano backend.
      MLP arguments: Namespace(batch_size=256, dataset='yelp', epochs=20, layers='[64,32,16,8]', learner='adam', lr=0.001,  num_neg=4,         out=1, path='Data/', reg_layers='[0,0,0,0]', verbose=1)
      Load Data done [10.3 s]. #user=19771, #item=48349, #train=908436, #test=19771
      Init: HR = 0.0805, NDCG = 0.0378 [11.1]
      Iteration 0 [412.4 s]: HR = 0.6410, NDCG = 0.4110, loss = 0.3279 [10.1 s]
      Iteration 1 [420.6 s]: HR = 0.7064, NDCG = 0.4834, loss = 0.2228 [9.8 s]
      Iteration 2 [434.5 s]: HR = 0.7391, NDCG = 0.5371, loss = 0.1957 [9.8 s]
      Iteration 3 [427.0 s]: HR = 0.7528, NDCG = 0.5579, loss = 0.1817 [10.0 s]
      Iteration 4 [428.2 s]: HR = 0.7739, NDCG = 0.5637, loss = 0.1717 [9.9 s]
      Iteration 5 [432.0 s]: HR = 0.7885, NDCG = 0.5802, loss = 0.1636 [9.9 s]
      Iteration 6 [432.4 s]: HR = 0.7995, NDCG = 0.6011, loss = 0.1575 [10.2 s]
      Iteration 7 [434.9 s]: HR = 0.8055, NDCG = 0.6053, loss = 0.1529 [10.0 s]
      Iteration 8 [437.1 s]: HR = 0.7966, NDCG = 0.6038, loss = 0.1487 [9.9 s]
      Iteration 9 [437.8 s]: HR = 0.8050, NDCG = 0.6121, loss = 0.1454 [10.0 s]
      Iteration 10 [442.7 s]: HR = 0.8163, NDCG = 0.6218, loss = 0.1421 [10.0 s]
      Iteration 11 [442.2 s]: HR = 0.8125, NDCG = 0.6266, loss = 0.1398 [11.1 s]
      Iteration 12 [448.1 s]: HR = 0.8163, NDCG = 0.6220, loss = 0.1374 [10.3 s]
      Iteration 13 [447.3 s]: HR = 0.8124, NDCG = 0.6156, loss = 0.1346 [10.0 s]
      Iteration 14 [450.0 s]: HR = 0.8197, NDCG = 0.6220, loss = 0.1327 [10.1 s]
      Iteration 15 [451.3 s]: HR = 0.8179, NDCG = 0.6265, loss = 0.1309 [10.1 s]
      Iteration 16 [455.3 s]: HR = 0.8126, NDCG = 0.6158, loss = 0.1289 [10.1 s]
      Iteration 17 [456.9 s]: HR = 0.8142, NDCG = 0.6260, loss = 0.1272 [10.0 s]
      Iteration 18 [461.0 s]: HR = 0.8106, NDCG = 0.6165, loss = 0.1255 [10.2 s]
      Iteration 19 [468.5 s]: HR = 0.8110, NDCG = 0.6185, loss = 0.1244 [9.9 s]
      End. Best Iteration 14:  HR = 0.8197, NDCG = 0.6220.
      The best MLP model is saved to Pretrain/yelp_MLP_[64,32,16,8]_1513114055.h5
      ```

