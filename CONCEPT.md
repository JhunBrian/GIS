## Enhancing Natural Disaster Response and Damage Assessment in Northern Mindanao through Satellite Imagery Data: A Focus on Image Segmentation Techniques

___

### Introduction

Natural disasters have long been a persistent challenge for communities worldwide, particularly those located within vulnerable regions such as Northern Mindanao in the Philippines. The region has experienced numerous devastating events like typhoons, earthquakes, and landslides, which have resulted in significant loss of life, property destruction, and economic hardship. To mitigate these impacts, it is crucial to develop innovative approaches for efficient and accurate natural disaster response and damage assessment. In line with this objective, we propose a novel approach utilizing advanced satellite imagery data processing techniques, specifically focusing on state-of-the-art image segmentation algorithms.

The current standard practice for assessing damages after natural disasters relies heavily upon field surveys conducted by trained personnel, often resulting in delayed responses due to safety concerns or logistical challenges. Moreover, traditional survey methods are time-consuming, laborious, and costly, making them less than ideal when rapid and large-scale evaluations are required. By leveraging high-resolution satellite imagery and automated image segmentation technologies, our proposed research aims to address these limitations and provide more effective solutions for enhancing natural disaster response and damage assessment efforts in Northern Mindanao.

Image segmentation refers to the process of partitioning digital images into multiple segments (i.e., groups of pixels) based on specific criteria, such as color, texture, or shape characteristics. These segments represent meaningful objects or features within the image, allowing for easier identification, classification, and quantification of damaged areas post-disaster. As a result, image segmentation offers great promise for improving the speed, accuracy, and efficiency of natural disaster response and damage assessment processes.

This research builds upon previous investigations exploring the use of remote sensing technology for disaster management applications, while also advancing the frontiers of image segmentation techniques for enhanced damage assessment capabilities. The proponent believe that this proposed approach holds tremendous potential for revolutionizing how natural disasters are managed in Northern Mindanao and beyond, ultimately leading to improved resilience and recovery outcomes.

In summary, this research proposal seeks to explore the application of cutting-edge image segmentation techniques using satellite imagery data to enhance natural disaster response and damage assessment efforts in Northern Mindanao. Through this endeavor, we aim to contribute valuable insights towards developing more robust, scalable, and sustainable strategies for managing future natural disasters in the region.

___

### Literature Review

*Traditional Response and Challenges from Natural Disasters in the Philippines*

The Philippines is highly vulnerable to natural disasters due to its geography, with the majority of the country's total land area and nearly three-fourths of the population vulnerable to multiple hazards such as typhoons, earthquakes, floods, storm surges, tsunamis, volcanic eruptions, and landslides[[2](https://www.worldbank.org/en/news/feature/2022/04/05/strengthening-the-philippines-post-disaster-financial-resilience-drmhubtokyo)]. In the past three decades, natural disasters have negatively impacted 120 million people and resulted in 33,000 deaths[[2](https://www.worldbank.org/en/news/feature/2022/04/05/strengthening-the-philippines-post-disaster-financial-resilience-drmhubtokyo)]. The country's disaster management practices have been assessed to be weak, particularly in financial utilization, information management, leadership, monitoring, collaboration, and coordination with various stakeholders[[3](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7587520/)]. The rehabilitation and recovery effort in the past has been the weakest[[3](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7587520/)]. The Philippines ranks ninth globally in terms of disaster risk, second highest among Asian countries[[2](https://www.worldbank.org/en/news/feature/2022/04/05/strengthening-the-philippines-post-disaster-financial-resilience-drmhubtokyo)].

*Integration of Computer Vision Technologies*

Recent research studies have explored the integration of computer vision technologies, particularly deep learning and satellite imagery, to improve natural disaster response. These studies propose automated damage assessment models using computer vision and deep learning techniques to provide rapid relief during disasters to the affected areas[[1](https://www.researchgate.net/publication/362504942_Flood_Disaster_Relief_Operation_A_Systematic_Literature_Review)][[3](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7587520/)]. The use of social media data and image analytics has also been explored to supplement satellite imagery in emergency response[[4](https://www.mdpi.com/2071-1050/15/11/8860)]. The studies demonstrate the capability of image analytics using social media as the image source to prioritize resources and assess the intensity of the population affected by a complex natural disaster[[4](https://www.mdpi.com/2071-1050/15/11/8860)]. The use of pre- and post-disaster satellite images to identify water-related building damages caused by natural disasters has also been proposed[[1](https://www.researchgate.net/publication/362504942_Flood_Disaster_Relief_Operation_A_Systematic_Literature_Review)][[3](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7587520/)]. These studies highlight the potential of computer vision technologies to enhance natural disaster response and recovery efforts.

By synthesizing these diverse bodies of literature, it is evident that there is a growing recognition of the potential benefits of data-driven approaches, such as computer vision and satellite imagery analysis, in enhancing natural disaster response and damage assessment capabilities. Building upon these foundations, the proposed research aims to leverage advanced image segmentation techniques to harness the power of satellite imagery data for more effective and efficient post-disaster assessment in Northern Mindanao.

___

### Preliminary Methodology

**Data Acquisition**

**Required Data**

The required data for this prject includes land cover data, land usage data, and information on residential and commercial areas. Land cover data is essential for understanding pre-existing conditions before a natural calamity occurs, while land usage data helps determine the vulnerability of residential and commercial areas during natural disasters. Identifying urban settlement patterns allows us to pinpoint critical locations where people live and work, enabling targeted damage assessment and prioritization of relief efforts.

**Satellite Imagery Data**

Comparative analyses between pre-calamity and post-calamity satellite imagery help reveal changes in land surface properties caused by natural disasters. The satellite imagery data will be gathered from Copernicus Browser and GeoMapper PH, which offer free access to high-quality satellite imagery covering Northern Mindanao. These resources provide reliable land cover maps, land usage data, and detailed layers depicting residential and commercial zones, allowing for the generation of precise and up-to-date information about the affected area. By utilizing these datasets, researchers can contribute to more informed decision-making and better-targeted interventions.

___

### Terminologies

- GIS: A geographic information system (GIS) is a computer system for capturing, storing, checking, and displaying data related to positions on Earth’s surface. GIS can show many different kinds of data on one map, such as streets, buildings, and vegetation. This enables people to more easily see, analyze, and understand patterns and relationships [[5](https://education.nationalgeographic.org/resource/geographic-information-system-gis/)].

- Satellite Imagery: (also Earth observation imagery, spaceborne photography, or simply satellite photo) are images of Earth collected by imaging satellites operated by governments and businesses around the world. Satellite imaging companies sell images by licensing them to governments and businesses such as Apple Maps and Google Maps[[6](https://en.wikipedia.org/wiki/Satellite_imagery)].

    - **Types of Satellite Imageries**:
        - *spatial resolution* is defined as the pixel size of an image representing the size of the surface area (i.e. m2) being measured on the ground, determined by the sensors' instantaneous field of view (IFOV);
        - *spectral resolution* is defined by the wavelength interval size (discrete segment of the Electromagnetic Spectrum) and number of intervals that the sensor is measuring;
        - *temporal resolution* is defined by the amount of time (e.g. days) that passes between imagery collection periods for a given surface location;
        - *Radiometric resolution* is defined as the ability of an imaging system to record many levels of brightness (contrast for example) and to the effective bit-depth of the sensor (number of grayscale levels) and is typically expressed as 8-bit (0–255), 11-bit (0–2047), 12-bit (0–4095) or 16-bit (0–65,535).
        - *Geometric resolution* refers to the satellite sensor's ability to effectively image a portion of the Earth's surface in a single pixel and is typically expressed in terms of Ground sample distance, or GSD. GSD is a term containing the overall optical and systemic noise sources and is useful for comparing how well one sensor can "see" an object on the ground within a single pixel. For example, the GSD of Landsat is ≈30m, which means the smallest unit that maps to a single pixel within an image is ≈30m x 30m. The latest commercial satellite (GeoEye 1) has a GSD of 0.41 m. This compares to a 0.3 m resolution obtained by some early military film based Reconnaissance satellite such as Corona.

____

Citations:

<p id="1">[1] https://www.researchgate.net/publication/362504942_Flood_Disaster_Relief_Operation_A_Systematic_Literature_Review</p>

<p id="2">[2] https://www.worldbank.org/en/news/feature/2022/04/05/strengthening-the-philippines-post-disaster-financial-resilience-drmhubtokyo</p>

<p id="3">[3] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7587520/</p>

<p id="4">[4] https://www.mdpi.com/2071-1050/15/11/8860</p>

<p id="5">[5] https://www.mdpi.com/2076-3263/8/5/165</p>

<p id="6">[5] https://education.nationalgeographic.org/resource/geographic-information-system-gis/</p>