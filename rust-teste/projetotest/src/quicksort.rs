pub fn quicksort_function(arr: &mut [i32]) {
    if arr.len() <= 1 {
        return;
    }

    let pivot_index = partition(arr);
    let (left, right) = arr.split_at_mut(pivot_index);
    quicksort_function(left);
    quicksort_function(&mut right[1..]);
}

fn partition(arr: &mut [i32]) -> usize {
    let pivot_index = arr.len() - 1;
    let pivot = arr[pivot_index];
    let mut i = 0;

    for j in 0..pivot_index {
        if arr[j] < pivot {
            arr.swap(i, j);
            i += 1;
        }
    }

    arr.swap(i, pivot_index);
    i
}