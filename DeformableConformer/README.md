# DeformableConformer Model Package
Author: dolphin-Dang

In this package we provide a class 'ModelRunner' to run the pretrained Deformable-Conformer model.

**TO MAKE THINGS CLEAR:  **
    If you don't want to change model structure,
    user only need to focus on ModelRunner class, and ignore other classes.

try:
    'from DeformableConformer import ModelRunner' to import the class.

ModelRunner provide two useful APIs:
    finetune: 
        Do short fine-tuning for cross-session tasks.
        Choices: (in config dictionary)
            Cover original .pth file every time or not.
            Use test set or not. 
                Without a test set, the ModelRunner will save the best training accuracy model.
                With a test set, the ModelRunner will save the best test accuracy model.
    inference: 
        Use preload model to do inference task.

You may want to check config dictionary for changing/learning some settings.


### Unimportant things
classes in this file:
    + PatchEmbedding (CNN)
    + MultiheadAttention
    + ResidualAdd
    + FeedForwardBlock
    + TransformerEncoderBlock
    + TransformerEncoder
    + ClassificationHead
    + DeformableCrossAttention
    + TransformerDecoderBlock
    + TransformerDecoder
    + DeformableConformer
    + ModelRunner

Deformable Conformer Structure:
    PatchEmbedding
    TransformerEncoder
        TransformerEncoderBlock
            ResidualAdd
            MultiheadAttention
            FeedForwardBlock
    TransformerDecoder
        TransformerDecoderBlock
            ResidualAdd
            DeformableCrossAttention
                MultiheadAttention
            FeedForwardBlock
    ClassificationHead
