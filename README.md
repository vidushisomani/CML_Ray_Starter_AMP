# Using Ray in CML

This AMP demonstrates Ray and its capabilities in CML. Ray is an open-source unified compute framework that makes it easy to scale AI and Python workloads.

## Troubleshooting Ray Cluster

Autoscale timeout
- Set the cluster.init timeout parameter to longer if starting the cluster timeout

Resource allocation
- Ensure your workspace/quota can handle the size of your ray head and workers

Ray Workers
- Check in the workspace sessions that your Ray Head and Workers are up and running. If not, refer to the notebook output to understand why this could be happening

Version Incompatibility
- Certain version of Ray work with certain versions of RayDP in order for Spark on Ray to work, similarly, there are specific verisons of Ray and Dask required for them to work together
- The python version that you are using in your CML session also makes a difference for each package, the recommended python version for this AMP is >= 3.8
- More information on version compatibility can be found here
https://docs.ray.io/en/latest/ray-more-libs/dask-on-ray.html
https://docs.ray.io/en/latest/ray-more-libs/raydp.html#installing-raydp

Ray Memory Usage Threshold (OutOfMemoryError)
- Based on the operation you are performing, adjust the memory allocated to the Ray Head and Ray Workers

Kernel Died Unexpectedly
- When this happens, it is best to restart your session, however, it will require you to start a new cluster and update the address accordingly