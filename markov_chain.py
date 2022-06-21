# Task 2: Markov Chain
import numpy as np
import matplotlib.pyplot as plt


def markov_chain(n, N):
    # initailize a n value as the number of entries
    # n = 5
    
    # 1. Construct a random n-vector 
    p = np.random.rand(n)
    # normalize the vector to the sum = 1 by divide each number by the sum
    p /= p.sum()
    
    
    # 2. Construct a random n × n (say n = 5) matrix with non-negative entries
    P = np.random.rand(n, n)
    # normalize to the sum for each row is 1
    P /= P.sum(axis=1)[:,None]
    
    
    
    # # 3. Compute the transition for N (say N = 50) steps
    # # initailize a N value as the number of steps
    # N = 50
    # # transition for N steps
    # for i in range (N):
    #     p1 = P.T.dot(p)
    
    
    # 4. Compute the eigenvector of P.T corresponding to the largest eigenvalue.
    evalue, evect = np.linalg.eig(P.T)
    
    # the largest eigenvalue
    maxeval = np.max(evalue)
    maxevect = evect[:, np.argmax(evalue)]
    
    # Rescale the entries of the eigenvector
    p_stationary = maxevect / np.sum(maxevect)
    
    
    # Compute the norm of p − pstationary and plot the norms against i.
    norm = np.zeros(N)
    for i in range(N):
        p = P.T.dot(p)
        norm[i] = (np.linalg.norm(p - p_stationary))
    
    # plot the norms against i.
    plt.plot(range(N),norm)
    plt.show()
    return p, norm

markov_chain(5, 50)
markov_chain(7, 100)
markov_chain(3, 20)
