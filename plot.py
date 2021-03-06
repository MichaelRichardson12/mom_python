# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:28:40 2017

@author: michael
"""

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import parameters as params
import numpy as np

def plot_mesh(node_coords):
    plt.figure(1)
    plt.title('Mesh')
    plt.xlabel(r'x-coordinates [$\lambda_{0}$]')
    plt.ylabel(r'y-coordinates [$\lambda_{0}$]')
    plt.plot(node_coords[:,0], node_coords[:,1], '-r')
    plt.axis('equal')
    x1,x2,y1,y2 = plt.axis()
    plt.axis((x1,x2,y1 - 2 ,y2 + 2))
    plt.grid(True)
    plt.show()
    
    
def plot_scatter(scattering):
    plt.figure(2)
    plt.title('2D RCS Real')
    plt.xlabel(r'$\phi$ [degrees]')
    plt.ylabel(r'$\sigma_{2D}$ [dB]')
    plt.plot(params.plot_angs, scattering.real, label='MoM')
    plt.grid(True)
    plt.show()
    
def plot_scat_polar(scattering):
    plt.figure(3)
    ax = plt.subplot(projection='polar')
    ax.plot(params.phi_fieldpoints, scattering)
    ax.set_rmax(np.max(scattering) + 5)
    ax.grid(True)
    ax.set_xlabel(r'$\phi$ [degrees]')
#    ax.set_ylabel(r'$\sigma_{2D}$ [dB]')
    ax.set_title("2D RCS Real", y=1.07)
    plt.show()
    
def plot_multiple_plots(data):
    
    x = np.arange(params.num_quads)
    ys = [ii + x + (ii*x)**2 for ii in range(10)]
    
    colors = cm.rainbow(np.linspace(0, 1, len(ys)))
    
    plt.figure(2)
    plt.title('2D RCS Real')
    plt.xlabel(r'$\phi$ [degrees]')
    plt.ylabel(r'$\sigma_{2D}$ [dB]')
    plt.grid(True)
    
    for ii in range(0, params.num_quads):
        plt.plot(params.plot_angs, data[ii][0].real, color=colors[ii], label="{} Gauss Quad".format(ii))
    
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    plt.show()