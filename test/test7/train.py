import torch
from torch import nn
torch.manual_seed(20260907)
x = torch.linspace(-1, 1, 101).reshape(-1, 1)
y = 3 * x- 1
model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)
for _ in range(200):
    pred = model(x)
    loss = loss_fn(pred, y)
#第一个TODO:
    #清空梯度
    opt.zero_grad()
    #反向传播
    loss.backward()
    #更新参数
    opt.step()
#第二个TODO：
#进入评估模式
model.eval()
#不计算梯度
with torch.no_grad():
    #计算最终结果
        pred = model(x)
        final_loss = loss_fn(pred, y)
        print("loss:", final_loss.item())
        print("weight:", model.weight.item())
        print("bias:", model.bias.item())
torch.save(model.state_dict(), "model.pt")