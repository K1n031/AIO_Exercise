import random
import math

def calculate_loss(num_samples, loss_name):
    num_samples = int(num_samples)
    
    samples = []
    predicts = []
    targets = []
    losses = []

    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        samples.append((predict, target))
        predicts.append(predict)
        targets.append(target)
        
        if loss_name == "MAE":
            loss = sum([abs(predict - target) for predict, target in samples]) / num_samples
        elif loss_name == "MSE":
            loss = sum([(predict - target) ** 2 for predict, target in samples]) / num_samples
        elif loss_name == "RMSE":
            loss = math.sqrt(sum([(predict - target) ** 2 for predict, target in samples]) / num_samples)
        
        losses.append(loss)

    print(f"Input number of samples ( integer number ) which are generated : {num_samples}")
    print(f"Input loss name : {loss_name}")
    for i in range(num_samples):
        print(f"loss name : {loss_name} , sample : {i} , pred : {predicts[i]} , target : {targets[i]} , loss : {losses[i]}")
    
    final_loss = losses[-1]
    print(f"final {loss_name} : {final_loss}")

num_samples = input("Input number of samples ( integer number ) which are generated: ")

if not num_samples.isnumeric():
    print("number of samples must be an integer number")
else:
    loss_name = input("Input the loss name (MAE, MSE, RMSE): ")

    calculate_loss(num_samples, loss_name)
