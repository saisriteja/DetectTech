

cats = {'ignored_regions': 0, 'pedestrian': 1, 'people': 2, 'bicycle': 3, 'car': 4, 'van': 5, 'truck': 6,
                    'tricycle': 7, 'awning-tricycle': 8, 'bus': 9, 'motor': 10, 'others': 11}

for i in cats.keys():
    print('target_class_config { \n  key: '+ i + ' \n     value: { \n      cov_center_x: 0.5 \n      cov_center_y: 0.5 \n      cov_radius_x: 0.4    \n  cov_radius_y: 0.4    \n  bbox_min_radius: 1.0\n   } \n }')
# d =   'target_class_config { \n  key: "pedestrian" \n     value: { \n      cov_center_x: 0.5 \n      cov_center_y: 0.5 \n      cov_radius_x: 0.4    \n  cov_radius_y: 0.4    \n  bbox_min_radius: 1.0\n   } \n }'
# print(d)