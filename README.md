# ![CC](https://camo.githubusercontent.com/8c6500c9b81793d2e5b86e03d4c0d26f5259c32984a90f7db03f8af5bccab303/68747470733a2f2f6769746875622e6769746875626173736574732e636f6d2f696d616765732f69636f6e732f656d6f6a692f756e69636f64652f31663337312e706e67) Calorie Counter
### Calorie Counter is saas app bringing more consciousness into food habits

# Table of contents
- [Implementation](#implementation)
- [Paper](#paper)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)

## ![gem](https://camo.githubusercontent.com/bf2f3b385cdfd8be9c670a2b1e7a7de8b1dd306d9f2acc3ffa0874fc2f5127b9/68747470733a2f2f6769746875622e6769746875626173736574732e636f6d2f696d616765732f69636f6e732f656d6f6a692f756e69636f64652f323731342e706e67) Implementation
- Food classification: dataset [food-101](https://www.kaggle.com/dansbecker/food-101), pytorch model [inceptionV3](https://pytorch.org/hub/pytorch_vision_inception_v3/)
- Salient object detection, based on [u^2 net](https://github.com/xuebinqin/U-2-Net) implementation
- Web server implemented on [FastAPI](https://fastapi.tiangolo.com/)
___
## ![mortar_board](https://github.githubassets.com/images/icons/emoji/unicode/1f393.png) Paper
[Calorie Counter: Recognition of food products,
    ready meals and their caloric values
    using neural networks.
    Poltavskiy A.V.](https://github.com/poltavski/CalorieCounter/blob/dev/CalorieCounter_paper.pdf)
___  
## ![demo](https://camo.githubusercontent.com/942a33e4caab9910e85d67311c8b20df5bf9e7711ed15ec95dafdf04ca98eb6c/68747470733a2f2f6769746875622e6769746875626173736574732e636f6d2f696d616765732f69636f6e732f656d6f6a692f756e69636f64652f31663338392e706e67) Live demo

**Visit portfolio to check [live demo](https://poltavski.github.io/projects/calorie_counter/)**

Screenshot from demo:
![demo-1](readme_images/demo.png)

## ![res](https://camo.githubusercontent.com/c3a4fcfba4d71d5b0f77f0faf063ecf3c589efc9bd212ab773b1224e974e11e9/68747470733a2f2f6769746875622e6769746875626173736574732e636f6d2f696d616765732f69636f6e732f656d6f6a692f756e69636f64652f31663461662e706e67) Results

<table>
  <tr>
    <td>Original image</td>
    <td>Recognized food</td>
  </tr>
  <tr>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_01-07-24_original.jpg?raw=true" width=500></td>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_01-07-24_strawberry_shortcake.jpg?raw=true" width=500></td>
  </tr>
  <tr>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_10-44-28_original.jpg?raw=true" width=500></td>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_10-44-28_result.jpg?raw=true" width=500></td>
  </tr>
  <tr>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_01-29-47_original.jpg?raw=true" width=500></td>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_01-29-47_ice_cream.jpg?raw=true" width=500></td>
  </tr>  
  <tr>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_10-47-31_original.jpg?raw=true" width=500></td>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_10-47-31_result.jpg?raw=true" width=500></td>
  </tr>
  
  <tr>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_10-42-12_original.jpg?raw=true" width=500></td>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_10-42-12_pork_chop.jpg?raw=true" width=500></td>
  </tr>
  <tr>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_01-28-55_original.jpg?raw=true" width=500></td>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_01-28-55_grilled_salmon.jpg?raw=true" width=500></td>
  </tr>  
  <tr>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_10-43-21_original.jpg?raw=true" width=500></td>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_10-43-21_result.jpg?raw=true" width=500></td>
  </tr>
  <tr>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_11-16-58_original.jpg?raw=true" width=500></td>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_11-16-58_chocolate_cake.jpg?raw=true" width=500></td>
  </tr>
  <tr>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_11-02-17_original.jpg?raw=true" width=500></td>
    <td><img src="https://github.com/poltavski/CalorieCounter/blob/dev/api/images/06-06-21_11-02-17_caesar_salad.jpg?raw=true" width=500></td>
  </tr>
</table>

___
## ![package](https://github.githubassets.com/images/icons/emoji/unicode/1f4e6.png) Installation
### Local deployment

- Launch pipenv environment & install dependencies
- Run server

### Docker image

- Build or Export container
- Run image

### Release (binary)

- Download Release from github
- Use local deployment section to run
___
## ![rocket](https://github.githubassets.com/images/icons/emoji/unicode/1f680.png) Usage

After deployment jump in web browser on configured or default (8000 or 8080) port

`http://0.0.0.0:8080/docs#/`

### [Food Image Labeling](http://0.0.0.0:8080/docs#/default)

#### Public endpoint for food image labeling by GET request.

### Args:

```
url: image url
percentage: show probabilities in percentage
```

### Returns:

```
Dictionary with image labels and probabilities
```

### Sample usage
#### Curl

```
curl -X 'GET' \
  'http://0.0.0.0:8080/image/label?url=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F36%2Fa3%2F2e%2F36a32e2efcfce9a2d5daa5ebf1a7b31e.jpg&percentage=true' \
  -H 'accept: application/json'
```

#### Request URL

http://0.0.0.0:8080/image/label?url=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F36%2Fa3%2F2e%2F36a32e2efcfce9a2d5daa5ebf1a7b31e.jpg&percentage=true

##### Response body with percentage = True

```
{
  "strawberry_shortcake": "95%",
  "red_velvet_cake": "2%",
  "chocolate_mousse": "1%",
  "creme_brulee": "1%",
  "panna_cotta": "1%"
}
```

##### Response body with percentage = False

```
{
  "strawberry_shortcake": 0.9516,
  "red_velvet_cake": 0.0154,
  "chocolate_mousse": 0.0071,
  "creme_brulee": 0.0058,
  "panna_cotta": 0.0058
}
```


___
### ![creds](https://camo.githubusercontent.com/15a4241f728815b9742f12cba069f7646e1e458913be6e7e50cded7384a2c0b5/68747470733a2f2f6769746875622e6769746875626173736574732e636f6d2f696d616765732f69636f6e732f656d6f6a692f756e69636f64652f303061392e706e67) Credits:
  Artem Poltavskiy 2021 (c). Visit my profile page for more: [poltavski.github.io](https://poltavski.github.io/)