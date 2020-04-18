/*
      * o1marker : price [0,4000]
      * o2marker : price [4000,8000]
      * o3marker : price [8000,12000]
      * o4marker : price [16000,20000]
      * o5marker : price [20000,24000]
      * o6marker : price [24000,28000]
      * o7marker : price [32000,36000]
      * o8marker : price [36000,40000]
      * o9marker : price [40000,45000]
      * o10marker : price [45000,50000]
      * o11marker : price [55000,60000]
      * o12marker : price [65000,70000]
      * o13marker : price [75000,80000]
      * o14marker : price [85000,90000]
      * o15marker : price [95000,100000]
      * o16marker : price [100000-]
* /

/**
 * @param price 均价
 * return 当前价格档次
 */

export function generateRange() {
  let range = [] // 22个等级
  let flag = 0
  for (let i = 1; i <= 100; i++) {
    if (i <= 10) {
      range.push({
        priceRange: i,
        min: flag,
        max: flag + 4000
      })
      flag = flag + 4000
    } else {
      range.push({
        priceRange: i,
        min: flag,
        max: flag + 5000
      })
      flag = flag + 5000
      if (flag > 95000) {
        break
      }
    }
  }
  return range
}

// export function judgePriceRange(price) {
//   const RANG = range.filter(item => price >= item.min && price < item.max)
//   return RANG[0].priceRange
// }
