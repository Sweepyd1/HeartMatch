# import asyncio
# from database.models import History, Action, Match
# from sqlalchemy import and_, or_

# class Observer:
#     def __init__(self, db, bot):
#         self.db = db
#         self.bot = bot
     
#     async def start_database_polling(self,):
#         try:
#             while True:
#                 await asyncio.sleep(45)
#                 await self.find_new_matches()
#         except asyncio.CancelledError:
#             print("Worker остановлен")

#     async def send_notify(self,user_1, user_2):
#         ...
    
#     async def find_new_matches(self):
#         async with self.db.get_session() as session:
#             subquery = (
#                 session.query(
#                     History.user_id.label('user_a'),
#                     History.selected_user_id.label('user_b')
#                 )
#                 .join(
#                     History, 
#                     and_(
#                         History.user_id == History.selected_user_id,
#                         History.selected_user_id == History.user_id,
#                         History.action == Action.like
#                     )
#                 )
#                 .outerjoin(
#                     Match,
#                     or_(
#                         and_(
#                             Match.user1_id == History.user_id,
#                             Match.user2_id == History.selected_user_id
#                         ),
#                         and_(
#                             Match.user1_id == History.selected_user_id,
#                             Match.user2_id == History.user_id
#                         )
#                     )
#                 )
#                 .filter(Match.match_id == None)
#                 .distinct()
#                 .subquery()
#             )

#             results = session.execute(subquery).fetchall()

#             for user_a, user_b in results:
#                 try:
#                     match = Match.create_sorted_pair(user_a, user_b)
#                     session.add(match)
#                     session.commit()
#                     # Отправляем уведомления
#                     await self.send_notify(user_a, user_b)
#                 except Exception as e:
#                     session.rollback()
#                     continue


    
      