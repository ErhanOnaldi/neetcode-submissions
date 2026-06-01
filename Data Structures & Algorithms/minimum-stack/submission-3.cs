public class MinStack 
{
    private Stack<int> s = new();
    private Stack<int> minS = new();

    public MinStack() { }
    
    public void Push(int val) {
        s.Push(val);
        if (minS.Count == 0 || val <= minS.Peek()) {
            minS.Push(val);
        } else {
            minS.Push(minS.Peek());
        }
    }
    
    public void Pop() {
        if (s.Count > 0) {
            s.Pop();
            minS.Pop();
        }
    }
    
    public int Top() {
        return s.Peek();
    }
    
    public int GetMin() {
        return minS.Peek();
    }
}