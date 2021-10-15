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
	"in_path":"../data/DIV2K_train_HR"
	,"out_path":"junyuan/HR_to_LR/results/DIV2K_train_LR_bicubic"
	,"noise_level":4
	,"process":
	{
	"process1":{
		"data_num_ratio": 1
		, "pipline":["downsample", "blur", "noise", "upsample", "sinc", "jpeg", "noise"]
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

The pipline can include the following properties:
- downsample
- upsample
- noise(random from `[0, noise_level]`)
- jpeg(random from `[jpeg_quality_l, jpeg_quality_h]`)
- blur(GaussianBlur from `[blur_sigma_down, blur_sigma_up]`)
- sinc_filter(can introduce ringing and overshoot artifacts)

2. Then run

`python demo.py -opt config/process.json`

## TODO

- [x] add sinc_filter
- [x] add rot_blur
- [ ] Multithreading Implementation