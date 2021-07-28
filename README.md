# HR_to_LR

scripts to process HR image to LR, you can customize the process.

## Dependencies

- opencv-python
- json

## Usage

1. First modify the json file in config/

Here is an example of the `process.json` file.
```
{
	"in_path":"/Users/liujunyuan/HR_to_LR/data/DIV2K_train_HR"
	,"out_path":"/Users/liujunyuan/HR_to_LR/results/DIV2K_train_LR_bicubic"
	,
	"process":
	{
	"process1":{
		"data_num_ratio": 1
		, "pipline":["downsample", "blur", "noise", "upsample", "jpeg", "noise"]
		, "downsample_method":"bicubic"
		, "downsample_scale": 0.5
		, "jpeg_quality_l": 30
		, "jpeg_quality_h": 95
		, "upsample_method":"bicubic"
		, "upsample_scale": 2
		}
	}
}
```

2. check `utils/load_data` to make sure you load the right json file.

```
def load_config():
    with open("config/test/bicubic.json") as f:
        config = json.load(f)
    return config
```

3. Then run

`python demo.py`