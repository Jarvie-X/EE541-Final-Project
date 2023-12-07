import torch
from matplotlib import pyplot as plt

def image_show(lr, srcnn, srgan, hr):
    # show the hr,lr and outputs images
    fig, axs = plt.subplots(1, 4, figsize=(20, 6))
    axs[0].imshow(lr)
    axs[1].imshow(srcnn)
    axs[2].imshow(srgan)
    axs[3].imshow(hr)
    
    axs[0].set_title('LR')
    axs[1].set_title('SRCNN(5-3-5)')
    axs[2].set_title('SRGAN')
    axs[3].set_title('HR')

    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])
    
    plt.show()