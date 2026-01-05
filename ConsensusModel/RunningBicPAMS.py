import pickle
from domain import Dataset, Biclusters
from mining import BicPAMS, Miner
from closing import Closer

if __name__ == '__main__':
    with open('PATH/to/Binary_matrix.pkl', 'rb') as f:
        data = pickle.load(f)
        miner = Miner(pattern='constant', stopConditions={'mincols': 3, 'minbics': , 'minsig':1}, niterations=1)
        closer = Closer(mergeOverlap=0.7, filterOverlap=0.5, order='area')
        bics = BicPAMS.run(data, miner, closer)
        open('biclustering_ouptut.txt', 'a').write(PATH/to/Biclusters.to_string(bics,data, detail=False))
        
        
#Given the lack of similarity, suspected to be due to a large impact of LD, a clustering approach, in an attempt to find what is common to all scores, was not viable. Therefore, it was decided to use a biclustering algorithm for the identification of the largest number of SNPs in the maximum possible number of PRS models.For this, an adaptation of the algorithm Biclustering based on PAttern Mining Software (BicPAMS) [60] was used. 

#This algorithm takes a n × m matrix as input, to then search for different types of patterns in the data. For this specific approach, a binary matrix was constructed where all the unique variants present in the PRS models were set as the rows and the PRS IDs as the columns. In this matrix context, a value of 1 denoted the presence of a SNP in a particular model, while a value of 0 indicated its absence.

#R. Henriques, F. L. Ferreira, and S. C. Madeira, “BicPAMS: Software for biological data analysis with pattern-based biclustering,” BMC Bioinformatics, vol. 18, no. 1, pp. 1–16, 2017. [Online]. Available:https://doi.org/10.1186/s12859-017-1493-3
