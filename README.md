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
	"in_path":"your location"
	,"out_path":"your location"
	,"noise_level":4
	,"poisson_level":30
	,"sinc_prob": 0.5
	,"multi-thread": false
	,"is_random": false
	,"process":
	{
	"process1":{
		"data_num_ratio": 1
		, "pipline":["downsample", "blur", "noise", "upsample", "sinc", "jpeg", "noise"]
		, "downsample_method":"bicubic"
		, "downsample_scale": 0.5
		, "blur_sigma_up": 0.8
		, "blur_sigma_down": 0.5
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
- noise(gauss noise sigma random from `[1, noise_level]`, and poisson noise from `[5, possion_level]` / 100)
- jpeg(random from `[jpeg_quality_l, jpeg_quality_h]`),now using opencv encode implementation
- blur(GaussianBlur from `[blur_sigma_down, blur_sigma_up]`)
- sinc_filter(can introduce ringing and overshoot artifacts)
- rot_blur(rotate image and then rotate back, can cause blur and edge artifacts)
- patch_noise(can add noise from a patch)
- fixed_downsample(sample method which fixes the size, the stable version of downsample/upsample)

to debug or steadily generate pictures, we suggest you set `"multi-thread": false`

2. Then run

`python demo.py -opt config/process.json`

## TODO

- [x] add sinc_filter
- [x] add rot_blur
- [x] add fixed_sample
- [x] add Multithreading Implementation
- [x] add different type of noise(now possion, gaussian, noise_multi)
- [x] add random mode
- [x] add random dropout prob mode