import opensimplex
import numpy
import dask
import dask.distributed #have to import this seperate because just importing dask won't include .distributed
import os


def create_arr():
    width = 10
    height = 10
    rng = numpy.random.default_rng(seed=0)
    ix, iy = rng.random(width), rng.random(height)  # generating a 1,000 by 1,000 array (takes ~8.6 seconds)
    arr = opensimplex.noise2array(ix, iy)
    return arr

if __name__ == '__main__':   #You have to write this or your PC will freak out.
    #if you use too many cores in your cluser on a potato pc, then your cluster wont work write. Like terminating workers and needing to run the tasks on a different worker.
    #dask is assigning 2 cores to an object. Like the raspberry pi's all zip tied up working together, it is called a cluster.
    cluster = dask.distributed.LocalCluster(n_workers=10, threads_per_worker=1)
    #the client object lets us use the cluster
    client = dask.distributed.Client(cluster)

    #we are lining our tasks up on the start line of the race.

    d1 = dask.delayed(create_arr)()  # Just pass the function reference here
    d2 = dask.delayed(create_arr)()
    d3 = dask.delayed(create_arr)()
    d4 = dask.delayed(create_arr)()
    d5 = dask.delayed(create_arr)()
    d6 = dask.delayed(create_arr)()
    d7 = dask.delayed(create_arr)()
    d8 = dask.delayed(create_arr)()
    d9 = dask.delayed(create_arr)()
    d10 = dask.delayed(create_arr)()
    
    
    # .compute is the gun shot that lets the horses know when to run! 4 cores will run create_arr() and save the arr to a letter variable 
    var = client.compute([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10], sync=True)

# only to create the txt document, doesn't change the output of the Texture Operator (TOP)
    counter = 1
    for i in var:
        f = open(("array{0}.txt".format(counter)), "w")
        f.write(str(i))
        counter +=1
        f.close()

# use script TOP to visualize

    #for item in var:
    #   copyNumpyArray(item) # Copies the contents of the numpyArary into the TOPs texture.
    
