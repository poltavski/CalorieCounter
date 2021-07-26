# Calorie Counter
### Calorie Counter is saas app bringing more consciousness into food habits

# Table of contents
- [Implementation](#implementation)
- [Paper](#paper)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)

## Implementation
- Food classification: dataset [food-101](https://www.kaggle.com/dansbecker/food-101), pytorch model [inceptionV3](https://pytorch.org/hub/pytorch_vision_inception_v3/)
- Salient object detection, based on [u^2 net](https://github.com/xuebinqin/U-2-Net) implementation
- Web server implemented on [FastAPI](https://fastapi.tiangolo.com/)

## Paper
[Calorie Counter: Recognition of food products,
    ready meals and their caloric values
    using neural networks.
    Poltavskiy A.V.](https://github.com/poltavski/CalorieCounter/blob/dev/CalorieCounter_paper.pdf)
  
## Results

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

## Installation
### Local deployment

- Launch pipenv environment & install dependencies
- Run server

### Docker image

- Build or Export container
- Run image

### Release (binary)

- Download Release from github
- Use local deployment section to run

## Usage

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



### Credits:
  Artem Poltavskiy 2021 (c). Visit my profile page for more: [poltavski.github.io](https://poltavski.github.io/)