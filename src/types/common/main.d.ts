export interface BobaProps {
  id: string;
  name: string;
  description: string;
  price: number;
  imageLink: string;
  defaultOptions?: {
    milk: string;
    toppings: Array<{ name: string; price: number }>;
  };
}

export interface OrderProps {
  order: BobaProps[];
  setOrder: (order: BobaProps[]) => void;
}

export interface CartItemCountProps {
  cartItemsCount: number;
}

export interface SearchBarProps {
  searchQuery: string;
  setSearchQuery: (searchQuery: string) => void;
}

export interface ToppingProps {
  name: string;
  price: number;
}

export interface ModalProps {
  bobaInfoModal: BobaProps;
  modalShow: boolean;
  milk: string;
  setMilk: (milk: string) => void;
  toppings: ToppingProps[];
  addTopping: (topping: string, checked: boolean) => void;
  onHide: () => void;
}
