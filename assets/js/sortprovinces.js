var colors_list = [];
var fill = function(idx) {
  return colors_list[idx];
}
var regions_list = {
  'North China': ['Beijing', 'Tianjin', 'Hebei', 'Shanxi', 'Inner Mongolia'],
  'Northeast China': ['Liaoning', 'Jilin', 'Heilongjiang'],
  'East China': ['Shanghai', 'Jiangsu', 'Zhejiang', 'Anhui', 'Fujian', 'Jiangxi', 'Shandong'],
  'South Central China': ['Henan', 'Hubei', 'Hunan', 'Guangdong', 'Guangxi', 'Hainan', 'Hong Kong', 'Macau'],
  'Southwest China': ['Chongqing', 'Sichuan', 'Guizhou', 'Yunnan', 'Tibet'],
  'Northwest China': ['Shaanxi', 'Gansu', 'Qinghai', 'Ningxia', 'Xinjiang'],
  'International': ['International']
};
var regions_colors = [
  colorbrewer.Greens[5].reverse(),
  colorbrewer.Reds[3].reverse(),
  colorbrewer.Blues[7].reverse(),
  colorbrewer.Oranges[8].reverse(),
  colorbrewer.Purples[5].reverse(),
  colorbrewer.YlOrRd[5].reverse(),
  colorbrewer.Greys[3]
];

function reprovinces(provinces) {
  var pro = [];
  var num = 0
  for (key in regions_list) {
    var n = 0;
    for (idx in regions_list[key]){
      var province = regions_list[key][idx];
      for (i in provinces) {
        if (province.toUpperCase() == provinces[i]['name'].toUpperCase()) {
          pro.push(provinces[i]);
          provinces.splice(i, 1);
          colors_list.push(regions_colors[num][n]);
          n = n + 1;
        }
      }
    }
    num = num + 1;
  }

  // pro = pro.concat(provinces);
  // colors_list = colors_list.concat(colorbrewer.Greys[provinces.length].reverse());
  return pro;
}
