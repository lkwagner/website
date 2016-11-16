---
layout: page
title: About
---

## Quantum Monte Carlo 

Our group has expertise in quantum Monte Carlo (QMC) techniques. 
The central quantity in the quantum mechanics of many particles is the many-body wave function, which is a complex function of *all* the positions of the quantum particles in the system.
For example, for 20 particles in 3 dimensions, this is a 60-dimensional function. 
Clearly we cannot represent such a function on a grid.

We use Monte Carlo techniques to handle the high dimensionality of the many-particle wave function.
In these techniques, the wave function is sampled instead of solved for directly. 
The two techniques that we use most are variational and projector Monte Carlo techniques. 
These methods have been around since near the beginning of computing, but only fairly recently can we use them on realistic materials.
For those that are interested, on my GitHub page, I have very simple implementations of these methods in Jupyter notebooks. 

For production calculations, we use QWalk, which is maintained within the group and available under the GPL version 2 at <a href="http://qwalk.org"> qwalk.org.</a>
The algorithms are not so different from the example notebooks above, except that QWalk runs much much faster, has a lot of bells and whistles, and can run efficiently on at least 1,000,000 processor threads, as tested on Argonne's supercomputer Mira.

We see QMC as the next step in simulations of materials. 
The current standard is density functional theory; while QMC methods are often 1000 times more expensive, they are also much more accurate and can use many processor cores. 

## Correlated electron systems

When electrons coordinate their motions, we term that effect electron correlation.
All systems of electrons are at least somewhat correlated.
For example, about half the cohesive energy of solids is due to electron correlation!
However, there are some systems for which the electron correlation plays an extremely important role. 
These are often, but not always, systems with transition metals.

Our group has used QMC techniques to study a number of different correlated electron systems, which range from the metal-insulator transition of VO<sub>2</sub> to the unconventional superconductors with copper and iron.
One of our big interests is whether one can classify these materials using genomic ideas.
For details, please see the papers tab.

## Low energy effective models


Effective models have a long history within physics as a way to better understand materials. 
They are a way to see commonalities between different physical systems; often while two systems may look quite different at first glance, one can find commonalities and encode them in effective models.
On the other hand, the effective models often contain undetermined parameters that must be somehow estimated or fit to experiment. 
In the face of limited experimental data on complex systems, there also can be competing models that all appear to have some advantages and disadvantages.

In collaboration with former postdoc Hitesh Changlani, we worked out a way to map first principles QMC calculations onto effective models. 
This method allows us not only to be able to find the parameters of the models, but also to make an assessment of their quality. 
We are currently working to automate and make systematic this technique so that it can be applied to many materials.
