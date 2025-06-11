

const binary_search = (arr: number[], target: number): number => {
  let low: number = 0;
  let high: number = arr.length;

  while (low <= high) {
    let mid: number = Math.floor((low + high) / 2);

    if (arr[mid] == target) {
      return mid;
    } else if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return -1;
};



const binary_search_recursive = (arr: number[], target: number, low: number, high: number): number => {
    if (low <= high) {
        let mid: number = Math.floor((low + high) / 2)
        if (arr[mid] == target) {
            return mid 
        } else if (arr[mid] < target) {
            return binary_search_recursive(arr, target, mid+1, high)
        } else {
            return binary_search_recursive(arr, target, low, mid-1)
        }
    }
    return -1; 
}

const arr: number[] = [2, 3, 4, 10, 40];
const target: number = 10;

console.log(binary_search(arr, target));
console.log(binary_search_recursive(arr, target, 0, arr.length)) 
