class Node:
    """ вершина бинарного дерева """
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    """ бинарное дерево"""
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        """рекурсивный поиск вершины"""
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True  # уже есть в дереве - игнор

        if value < node.data:  # рекурсия по левой ветви
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:  # рекурсия по правой ветви
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False  # нашли искомый узел, к которому надо добавить новое значение

    def append(self, obj):
        """ добавление вершины
        если новое значение меньше значения в родительском узле - добавляем в левую ветвь, если больще-  в правую
        Если значение уже есть в дереве - то игнорируем его(отсутствие дублей)"""
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)  # рекурсивный поиск врешины к которой добавляем

        if not fl_find and s:  # значения нет в дереве(fl_find), добавляем к вершине объекта S
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        """ отображение бинарного дерева рекурсия в один столбец """
        if node is None:
            return

        self.show_tree(node.right)
        print(node.data)
        self.show_tree(node.left)

    def show_wide_tree(self, node):
        """отображение дерева в ширину"""
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def __del_leaf(self, s, p):
        """"удаление листа в дереве: удаляем связь от родителя к этому листу"""
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        """удаление вершины с одним потомком: связь между родителем и удаляемой вершиной
        переопределяем на ее единственного потомка"""
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        """поиск минимального значения в поддереве"""
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def del_node(self, key):
        """удаление узла"""
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None # вершина не найдена, удалять нечего

        if s.left is None and s.right is None:  # вершина листовая - нет потомков
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None: # есть либо правый либо левый потомок
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)  # sr - min  в правом поддереве   pr - родит эл-т для этого минимума
            s.data = sr.data  # s - удаляемая вершина 
            self.__del_one_child(sr, pr)



v = [9, 6,8,15,12,3,19,11]

t = Tree()
for x in v:
    t.append(Node(x))
t.show_wide_tree(t.root)
t.del_node(8)
print()
t.show_wide_tree(t.root)