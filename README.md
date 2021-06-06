# Calorie Counter
### Calorie Counter is saas app bringing more consciousness into food habits

## Implementation:
- Food classification: dataset [food-101](https://www.kaggle.com/dansbecker/food-101), pytorch model [inceptionV3](https://pytorch.org/hub/pytorch_vision_inception_v3/)
- Salient object detection, based on [u^2 net](https://github.com/xuebinqin/U-2-Net) implementation
- Web server implemented on [FastAPI](https://fastapi.tiangolo.com/)


## Results:

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

### TO-DO:
 - Add pipenv setup
 - Add thesis
 - Build package

### Credits:
  Artem Poltavskiy 2021 (c). Visit my profile page for more: [poltavski.github.io](https://poltavski.github.io/)