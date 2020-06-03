if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)

    def find_runner_up(arr,n):
        winner = -100
        runner_up = -101
        for x in range(0,n):
            if arr[x] > winner:
                runner_up = winner
                winner = arr[x]
            elif winner >= arr[x] and arr[x] > runner_up:
                runner_up = arr[x]
            else:
                continue
        return runner_up
    
    print(find_runner_up(arr, n))
