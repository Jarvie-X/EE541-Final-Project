import torch
from matplotlib import pyplot as plt

def image_show(hr,lr,outputs):
    # show the hr,lr and outputs images
    fig, axs = plt.subplots(1, 3, figsize=(20, 8))
    axs[0].imshow(hr)
    axs[1].imshow(lr)
    axs[2].imshow(outputs)
    
    axs[0].set_title('HR')
    axs[1].set_title('LR')
    axs[2].set_title('SRCNN')

    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])
    
    plt.show()