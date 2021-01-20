from django.db import models, DataError, IntegrityError

import uuid

from authentication.models import CustomUser
from author.models import Author
from book.models import Book


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    end_at = models.DateTimeField(null=True)
    plated_end_at = models.DateTimeField()

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        return str(self.to_dict())[1:-1]

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    def to_dict(self):

        return {
            'id': self.id,
            'user': self.user,
            'book': self.book,
            'created_at': str(self.created_at),
            'end_at': str(self.end_at) if self.end_at else self.end_at,
            'plated_end_at': str(self.plated_end_at)
        }

    @staticmethod
    def create(user, book, plated_end_at):
        try:
            if book.count:
                order = Order(user=user, book=book, plated_end_at=plated_end_at)
                book.count -= 1
                book.save()
                order.save()
                return order
        except (IntegrityError, AttributeError, DataError, ValueError) as err:
            # print(err)
            # LOGGER.error("Wrong attributes or relational integrity error")
            return None

    @staticmethod
    def get(**kwargs):
        try:
            order = Order.objects.get(**kwargs)
            return order
        except Order.DoesNotExist:
            return None

    @staticmethod
    def get_by_id(order_uuid):
        try:
            order = Order.objects.get(uuid=order_uuid)
            return order
        except Order.DoesNotExist:
            pass

    def update(self, plated_end_at=None, end_at=None):
        if plated_end_at:
            self.plated_end_at = plated_end_at
        if end_at:
            self.end_at = end_at
        self.save()

    @staticmethod
    def get_all():
        all_order = Order.objects.all()
        return all_order

    @staticmethod
    def get_not_returned_books():
        orders = [order for order in Order.get_all() if order.end_at is None]
        return orders

    @staticmethod
    def get_not_returned_books_for_user(user_id):
        orders = Order.objects.filter(end_at=None, user_id=user_id)
        return orders

    @staticmethod
    def delete_by_id(order_uuid):
        """
        :param order_uuid: an id of an order to be deleted
        :type order_uuid: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """

        try:
            user = Order.objects.get(uuid=order_uuid)
            user.delete()
            return True
        except Order.DoesNotExist:
            # LOGGER.error("User does not exist")
            pass
        return False
