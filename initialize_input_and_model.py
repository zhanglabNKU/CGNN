import numpy as np
import torch
import torch.nn as nn

'''
For heterogeneous network data, the input of CGNN is as follows:
    
    adjacent matrix for gene:
    gene_adj: lnc_adj.pth, mic_adj.pth
    similarity matrix for gene:
    gene_wei: lnc_wei.pth, mic_wei.pth  

    adjacent matrix for disease:
    dis_adj: disForlnc_adj.pth, disFormic_adj.pth
    similarity matrix for disease:
    dis_wei: disForlnc_wei.pth, disFormic_wei.pth  
    
    train samples of gene-disease associations:
    train_sample: train_lncdis.txt, train_micdis.txt  
    validation samples of gene-disease associations:
    valid_sample: valid_lncdis.txt, valid_micdis.txt  
    test samples of gene-disease associations:
    test_sample:  test_lncdis.txt, test_micdis.txt  
    
    conduit type for train samples:
    train_group: ld_train_group.txt, md_train_group.txt  
    conduit type for validation samples:
    valid_group: ld_valid_group.txt, md_valid_group.txt  
    conduit type for test samples:
    test_group:  ld_test_group.txt, md_test_group.txt  
    
    initial word embedding of gene node:
    gene_node_embedding: lnc_node_embedding.pth, mic_node_embedding.pth  
    initial word embedding of disease node:
    dis_node_embedding: disForlnc_node_embedding.pth, disFormic_node_embedding.pth
    
    labels for train samples:
    train_label: ld_train_label.txt, md_train_label.txt
    labels for validation samples:
    valid_label: ld_valid_label.txt, md_valid_label.txt
    labels for test samples:
    test_label:  ld_test_label.txt, md_test_label.txt
    
'''

'''
    
For homogeneous network data, the input of CGNN is as follows:
    
    graph num denotes which subgraph
    graph_num: 'graph'+'i', i=1,2,3,4 
    
    graph node denotes nodes belonging to subgraph
    graph_node: graph_num graph node.txt
    
    adjacent matrix for subgraph
    adj_matrix: graph_num+ppi adj matrix.pth, graph_num+ddi adj matrix.pth
    
    norm adjacent matrix for subgraph
    norm_matrix: graph_num+ppi norm matrix.pth, graph_num+ddi norm matrix.pth

    degree matrix for subgraph
    degree_matrix: graph_num+degree matrix.pth
    
    train sample for subgraph
    train_sample: graph_num+ train_sample.txt
    
    test sample for subgraph
    test_sample: graph_num+ test_sample.txt
    
    conduit type for train sample
    train_group: graph_num+ train_group.txt
    
    conduit type for test sample
    test_group: graph_num+ test_group.txt
    
    initial embedding of all nodes for PPI and DDI
    all_node_embedding: all_node_embedding.pth
    
    node_embedding for graph_num subgraph: 
        
        graph_node_tensor = torch.tensor(graph_node)

        graph_node_embedding = all_node_embedding[graph_node_tensor,:]
        
    label for train sample
    train_label: graph_num+ train_label.txt
    
    label for test sample
    test_label: graph_num+ test_label.txt
'''
'''
For heterogeneous network data and homogeneous network data, the labels are as follows, 
where loss function needs the type of label is float.
'''

tensor_train_label = torch.tensor(train_label).float().cuda()

tensor_vali_label = torch.tensor(valid_label).float() # only for heterogeneous networks

tensor_test_label = torch.tensor(test_label).float()

'''
Initializing CGNN model, optimizer and loss function.
'''

conduit_GNN = conduitGNN()

optm = torch.optim.Adam(conduit_GNN.parameters(), lr=0.01)

BCE = nn.BCELoss()

'''
When computing the loss of CGNN, we should add up regularization loss.
'''

loss = BCE(train_output, tensor_train_label) + regu(lambda1, lambda2).cuda()



