
const linearSearch = (arr: number[], target: number) => {
    const arr_length: number = arr.length; 
    let i: number = 0; 
    for (i; i <= arr_length; i = i + 1){
        if (arr[i] == target) {
            return i; 
        }
    }

}


const linearSearchRecure = (arr: number[], target: number, index:number = 0): number =>{
    if (index === arr.length) {
        return -1; 
    }
    if (arr[index] == target) {
        return index; 
    }

    return linearSearchRecure(arr, target, index+1)
}

const arr: number[] = [10, 23, 45, 70, 11, 15]
const target: number = 70 
 
console.log(linearSearch(arr, target)) 

console.log(linearSearchRecure(arr, target)) 