# HR_to_LR

scripts to process HR image to LR, you can customize the process.

## Dependencies

- opencv-python
- json

## Usage

1. First modify the json file in config/

Here is an example of the process.
```
"process1":{
	"data_num_ratio": 2
	, "pipline":["downsample", "blur", "jpeg", "noise", "upsample", "jpeg"]
	, "downsample_method":"bicubic"
	, "downsample_scale": 0.5
	, "jpeg_quality": 50
	, "upsample_method":"bicubic"
	, "upsample_scale": 2
	}
```

2. Then run

`python demo.py`