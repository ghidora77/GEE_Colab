def mask_Landsat8SR_2(image, timeField):
    # Bits 3 and 5 are cloud shadow and cloud, respectively.
    cloudShadowBitMask = (1 << 3)
    cloudsBitMask = (1 << 5)
    # Get the pixel QA band.
    qa = image.select('pixel_qa')
    # Both flags should be set to zero, indicating clear conditions.
    mask = (
        qa.bitwiseAnd(cloudShadowBitMask).eq(0)
            and
        (qa.bitwiseAnd(cloudsBitMask).eq(0)))
    
    val = (image.updateMask(mask).divide(10000)
      .select('B[0-9]*')
      .copyProperties(image, [timeField]))
    
    return val




