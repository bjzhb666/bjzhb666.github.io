---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hello! I am a Ph.D student at [Institute of Automation, Chinese Academy of Sciences (CASIA)](http://www.ia.cas.cn/). Before that, I got B.Eng from Beijing Institute of Technology.

My research interests mainly lie in **Post Training of Multimodal Large Language Models** (SFT, RLHF, RLVR, OPD), **Model Editing** (continual learning and machine unlearning), and **Computer Vision**. I have published papers at top AI conferences with total <a href='https://scholar.google.com/citations?user=Gs22F0UAAAAJ&hl=en'>Google Scholar citations <strong><span id='total_cit'>0+</span></strong></a> <a href='https://scholar.google.com/citations?user=Gs22F0UAAAAJ&hl=en'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.


To know more about me, please visit my [Google Scholar](https://scholar.google.com/citations?user=Gs22F0UAAAAJ&hl=en) and [GitHub](https://github.com/bjzhb666). Any discussion is welcome via [E-mail](mailto:zhaohongbo2022@ia.ac.cn).

# 🔥 News

- *2026.01*: &nbsp;🎉🎉 [Practical Continual Forgetting](https://arxiv.org/abs/2501.09705) is accepted by **IEEE T-PAMI 2026**!
- *2025.06*: &nbsp;🎉🎉 [MLLM-CL](https://arxiv.org/abs/2506.05453) is released, a benchmark for continual learning in multimodal large language models. [[Code](https://github.com/bjzhb666/MLLM-CL)]
- *2025.02*: &nbsp;🎉🎉 [MRS Sampler](https://arxiv.org/abs/2502.07856) is accepted by **ICLR 2025** as a **spotlight**!
- *2024.09*: &nbsp;🎉🎉 [OpenSatMap](https://arxiv.org/abs/2410.23278) is accepted by **NeurIPS 2024** Datasets and Benchmarks Track. [[Code](https://opensatmap.github.io/)]
- *2024.03*: &nbsp;🎉🎉 [GS-LoRA](https://arxiv.org/abs/2403.11530) and [LingoCL](https://openaccess.thecvf.com/content/CVPR2024/papers/Ni_Enhancing_Visual_Continual_Learning_with_Language-Guided_Supervision_CVPR_2024_paper.pdf) are accepted by **CVPR 2024**. [[Code](https://github.com/bjzhb666/GS-LoRA)]

# 📝 Publications

## Journal Papers

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">T-PAMI 2026</div><img src='images/pcf.png' alt="Practical Continual Forgetting" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Practical Continual Forgetting for Pre-trained Vision Models](https://arxiv.org/abs/2501.09705)

**Hongbo Zhao**, Fei Zhu, Bolin Ni, Feng Zhu, Gaofeng Meng, Zhaoxiang Zhang

*IEEE Transactions on Pattern Analysis and Machine Intelligence (T-PAMI), 2026*

[**Paper**](https://arxiv.org/abs/2501.09705) \| [**Code**](https://github.com/bjzhb666/GS-LoRA)

</div>
</div>



## Conference Papers

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2024</div><img src='images/gs_lora.png' alt="GS-LoRA" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Continual Forgetting for Pre-trained Vision Models](https://arxiv.org/abs/2403.11530)

**Hongbo Zhao**, Bolin Ni, Junsong Fan, Yuxi Wang, Yuntao Chen, Gaofeng Meng, Zhaoxiang Zhang

*IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024*

[**Paper**](https://arxiv.org/abs/2403.11530) \| [**Code**](https://github.com/bjzhb666/GS-LoRA)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/opensatmap.png' alt="OpenSatMap" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[OpenSatMap: A Fine-grained High-resolution Satellite Dataset for Large-scale Map Construction](https://arxiv.org/abs/2410.23278)

**Hongbo Zhao**, Lue Fan, Yuntao Chen, Haochen Wang, Xiaojuan Jin, Yixin Zhang, Gaofeng Meng, Zhaoxiang Zhang

*Neural Information Processing Systems (NeurIPS), 2024 (Datasets and Benchmarks Track)*

[**Paper**](https://arxiv.org/abs/2410.23278) \| [**Project**](https://opensatmap.github.io/)

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025 Spotlight</div><img src='images/mrs_sampler.png' alt="MRS Sampler" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MRS: A Fast Sampler for Mean Reverting Diffusion based on ODE and SDE Solvers](https://arxiv.org/abs/2502.07856)

Ao Li, Wei Fang, **Hongbo Zhao**, Le Lu, Ge Yang, Minfeng Xu

*International Conference on Learning Representations (ICLR), 2025 (Spotlight)*

[**Paper**](https://arxiv.org/abs/2502.07856)

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2024</div><img src='images/lingocl.png' alt="LingoCL" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Enhancing Visual Continual Learning with Language-Guided Supervision](https://openaccess.thecvf.com/content/CVPR2024/papers/Ni_Enhancing_Visual_Continual_Learning_with_Language-Guided_Supervision_CVPR_2024_paper.pdf)

Bolin Ni, **Hongbo Zhao**, Chenghao Zhang, Ke Hu, Gaofeng Meng, Zhaoxiang Zhang, Shiming Xiang

*IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024*

[**Paper**](https://openaccess.thecvf.com/content/CVPR2024/papers/Ni_Enhancing_Visual_Continual_Learning_with_Language-Guided_Supervision_CVPR_2024_paper.pdf)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2026</div><img src='images/rft_forgetting.png' alt="RFT Forgetting" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Reinforcement Fine-Tuning Naturally Mitigates Forgetting in Continual Post-Training](https://arxiv.org/abs/2507.05386)

Song Lai, Haohan Zhao, Rong Feng, Changyi Ma, Wenzhuo Liu, **Hongbo Zhao**, Xi Lin, Dong Yi, Qingfu Zhang, Hongbin Liu, et al.

*International Conference on Machine Learning (ICML), 2026*

[**Paper**](https://arxiv.org/abs/2507.05386)

</div>
</div>


## Preprints

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/mllm_cl.png' alt="MLLM-CL" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MLLM-CL: Continual Learning for Multimodal Large Language Models](https://arxiv.org/abs/2506.05453)

**Hongbo Zhao**, Fei Zhu, Haiyang Guo, Meng Wang, Rundong Wang, Gaofeng Meng, Zhaoxiang Zhang

*arXiv preprint, 2025*

[**Paper**](https://arxiv.org/abs/2506.05453) \| [**Code**](https://github.com/bjzhb666/MLLM-CL)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/vtcbench.png' alt="VTCBench" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[VTCBench: Can Vision-Language Models Understand Long Context with Vision-Text Compression?](https://arxiv.org/abs/2512.15649)

**Hongbo Zhao**, Meng Wang, Fei Zhu, Wenzhuo Liu, Bolin Ni, Fanhu Zeng, Gaofeng Meng, Zhaoxiang Zhang

*arXiv preprint, 2025*

[**Paper**](https://arxiv.org/abs/2512.15649)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/mcitlib.png' alt="MCITLib" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MCITLib: Multimodal Continual Instruction Tuning Library and Benchmark](https://arxiv.org/abs/2508.07307)

Haiyang Guo, Fei Zhu, **Hongbo Zhao**, Fanhu Zeng, Wenzhuo Liu, Shijie Ma, Da-Han Wang, Xu-Yao Zhang

*arXiv preprint, 2025*

[**Paper**](https://arxiv.org/abs/2508.07307)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/cl_survey.png' alt="CL Survey" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[A Comprehensive Survey on Continual Learning in Generative Models](https://arxiv.org/abs/2506.13045)

Haiyang Guo, Fanhu Zeng, Fei Zhu, Jiayi Wang, Xukai Wang, Jingang Zhou, **Hongbo Zhao**, Wenzhuo Liu, Shijie Ma, Xu-Yao Zhang, et al.

*arXiv preprint, 2025*

[**Paper**](https://arxiv.org/abs/2506.13045)

</div>
</div>


# 📖 Education

- *2022.09 - Present*, Ph.D. in Pattern Recognition and Intelligent System, **Institute of Automation, Chinese Academy of Sciences (CASIA)**.
- *2018.09 - 2022.07*, B.Eng. in Automation, **Beijing Institute of Technology (BIT)**.

# 🎖 Academic Activities

**Conference Reviewer:** CVPR, ICCV, ECCV, ICML, NeurIPS, ICLR, AISTATS

**Journal Reviewer:** T-PAMI, IJCV, T-MM, SCIENTIA SINICA Informationis
