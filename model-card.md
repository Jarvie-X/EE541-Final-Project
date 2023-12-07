# Model card for "EE541 Project on Super Resolution"

Jump to section:

- [Model details](#model-details)
- [Intended use](#intended-use)
- [Factors](#factors)
- [Metrics](#metrics)
- [Evaluation data](#evaluation-data)
- [Training data](#training-data)
- [Quantitative analyses](#quantitative-analyses)
- [Ethical considerations](#ethical-considerations)
- [Caveats and recommendations](#caveats-and-recommendations)

## Model details

_Basic information about the model._

- Person or organization developing model
  Hengyi Tang and Jiawei Xiang
- Model date
  12/6/2023
- Model version
  1.0
- Model type
  Convolutional neural network and Generative adversarial network of deep learning
- Information about training algorithms, parameters, fairness constraints or other applied
  approaches, and features
  Using learning rate decay strategy


## Intended use

_Use cases that were envisioned during development._

### Primary intended uses
Given a low-resolution image, return a higher-resolution verison of it.

### Primary intended users
People who wants to enhance enhance a low-resolution (LR) image to an image of higher-resolution.


## Factors

### Relevant factors
- Groups: Low-resolution images and high-resolution images
- Instrumentation: the hardware and software of camera, which was used to take the image of input
- Environment: hardware resources, memory constraints and preprocessing requirements
### Evaluation factors
- SNR: This shows how serious the original image is affected by the added noise. The greater the SNR is, the better quality the output images have.
- PSNR: This uses the peak dynamic range, such as 255 for an 8 bit image and measures the contrast in the region of interest better.
- SSIM: A perceptual metric to measure the structural similarity between 2 images.
## Metrics

_The appropriate metrics to feature in a model card depend on the type of model that is being tested.
For example, classification systems in which the primary output is a class label differ significantly
from systems whose primary output is a score. In all cases, the reported metrics should be determined
based on the model’s structure and intended use._

### Model performance measures
- SNR: This shows how serious the original image is affected by the added noise. The greater the SNR is, the better quality the output images have.
- PSNR: This uses the peak dynamic range, such as 255 for an 8 bit image and measures the contrast in the region of interest better.
- SSIM: A perceptual metric to measure the structural similarity between 2 images.

### Decision thresholds
- Quality assessment: assess the quality of the super-resolved images.

## Evaluation data

_All referenced datasets would ideally point to any set of documents that provide visibility into the
source and composition of the dataset. Evaluation datasets should include datasets that are publicly
available for third-party use. These could be existing datasets or new ones provided alongside the model
card analyses to enable further benchmarking._

### Datasets
The "DIV2K_valid_HR" and "DIV2K_valid_LR_bicubic_X2" were used to evaluate the model.

### Motivation
All the diverse images have been randomly picked up from the internet ranging from people, handmade objects and environments, to flora and fauna, and natural scenes including underwater and dim light conditions. And we got the low images by the same downgrading operation as what we did in the train and validation datasets.

### Preprocessing
Resized the low and high-resolution images to (128, 128) pixels and (256, 256) pixels to make the images adapt to the model. 

## Training data

The training data hosts a variety of down-sampled RGB images and their corresponding high resolution images. The image down-sampling is to remove an equal number of rows and columns
of an image by a factor of 2. All the diverse images have been randomly picked up from the internet ranging from people, handmade objects and environments, to flora and fauna, and natural scenes including underwater and dim light conditions.

## Quantitative analyses

_Quantitative analyses should be disaggregated, that is, broken down by the chosen factors. Quantitative
analyses should provide the results of evaluating the model according to the chosen metrics, providing
confidence interval values when possible._

### Unitary results
[model,	        [dataset,  SNR,	     PSNR,	   SSIM]]:
[SRCNN (9-1-5), [train,	  21.7361,	 28.0684,	 0.9019],
	              [valid,	 21.3034,	 27.8302,	 0.8987],
	              [test,	 21.2288,	 27.9970,	 0.8972]]
[SRCNN (5-3-5),	[train,	 22.0658,	 28.3980,	 0.9120],
	              [valid,	 21.6212,	 28.1480,	 0.9088],
	              [test,	 21.3350,	 28.1032,	 0.8983]]
[SRGAN,	        [train,	 20.1957,	 26.5279,	 0.8769],
	              [valid,	 19.7888,	 26.3156,	 0.8735],
	              [test,	 19.5455,	 26.3137,	 0.8726]]

## Ethical considerations

_This section is intended to demonstrate the ethical considerations that went into model development,
surfacing ethical challenges and solutions to stakeholders. Ethical analysis does not always lead to
precise solutions, but the process of ethical contemplation is worthwhile to inform on responsible
practices and next steps in future work._

### Data
The dataset contains some photos of individules. This may violate the portrait right.

### Human life
When this model are used by medical professionals in imaging technologies like MRI, CT scans, and microscopy, this informs decisions about human health.

### Mitigations
Implement data privacy and security measures to protect sensitive information in the training data by training our model on our own PCs.
Stay informed about legal requirements related to data privacy, informed consent, and other ethical considerations.

### Risks and harms
This model may inadvertently enhance details in images, potentially revealing sensitive information that was not visible in the original low-resolution images or was mosaicin the original images. This raises privacy concerns, especially if this model is applied to images without the knowledge or consent of individuals.
There is a risk of the super-resolution model inaccurately enhancing certain features, leading to unrealistic or incorrect details in the output images. This is particularly crucial in applications where accuracy is paramount, such as medical imaging.

### Use cases
Eliminating mosaic.

## Caveats and recommendations

_This section should list additional concerns that were not covered in the previous sections._



