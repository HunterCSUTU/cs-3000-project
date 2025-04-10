import opensimplex
import numpy
import dask
import dask.distributed #have to import this seperate because just importing dask won't include .distributed


def create_arr():
    rng = numpy.random.default_rng(seed=0)
    ix, iy = rng.random(100), rng.random(100)  # generating a 1,000 by 1,000 array (takes ~8.6 seconds)
    arr = opensimplex.noise2array(ix, iy)
    return arr

if __name__ == '__main__':
    #if you use too many cores in your cluser on a potato pc, then your cluster wont work write. Like terminating workers and needing to run the tasks on a different worker.
    #dask is assigning 2 cores to an object. Like the raspberry pi's all zip tied up working together, it is called a cluster.
    cluster = dask.distributed.LocalCluster(n_workers=2, threads_per_worker=1)
    #the client object lets us use the cluster
    client = dask.distributed.Client(cluster)

    #we are lining our tasks up on the start line of the race.
    d1 = dask.delayed(create_arr)()  # Just pass the function reference here
    d2 = dask.delayed(create_arr)()  # No parentheses, because we want to delay the call


    # .compute is the gun shot that lets the horses know when to run! 4 cores will run create_arr() and save the arr to a letter variable 
    a, b = client.compute([d1, d2], sync=True)

    print(f"a:{a},\n\n b:{b}\n")

