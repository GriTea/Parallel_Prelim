import serial_convolution
import parallel_convolution
import time

def main():
    folder_of_images = 'dog_train'  
    number_of_iterations = int(input("Please input number of iterations: "))
    results = []
    
    for iteration in range(number_of_iterations):
        
        number_of_images = int(input(f"Please input number of images for iteration {iteration + 1}: "))
        serial_time = serial_convolution.process_images_serial(folder_of_images, number_of_images)
        parallel_time = parallel_convolution.process_images_parallel(folder_of_images, number_of_images)
        speedup = serial_time / parallel_time if parallel_time > 0 else float('inf')
        
        results.append({
            'Iteration': iteration + 1,
            'Images': number_of_images,
            'Serial Time (ms)': round(serial_time, 4),
            'Parallel Time (ms)': round(parallel_time, 4),
            'Speedup': round(speedup, 4)
        })
    
    
    print("\nResults Table:")
    print("{:<10} {:<10} {:<20} {:<20} {:<10}".format('Iteration', 'Images', 'Serial Time (ms)', 'Parallel Time (ms)', 'Speedup'))
    for result in results:
        print("{:<10} {:<10} {:<20} {:<20} {:<10}".format(result['Iteration'], result['Images'], result['Serial Time (ms)'], result['Parallel Time (ms)'], result['Speedup']))






if __name__ == "__main__":
    main()
