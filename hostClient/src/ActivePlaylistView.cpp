/**
 * Copyright 2011 Kurtis L. Nusbaum
 * 
 * This file is part of UDJ.
 * 
 * UDJ is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 * 
 * UDJ is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with UDJ.  If not, see <http://www.gnu.org/licenses/>.
 */
#include "ActivePlaylistView.hpp"
#include "DataStore.hpp"
#include <QHeaderView>
#include <QSqlRecord>
#include <QSqlField>
#include "ActivePlaylistDelegate.hpp"
#include "ActivePlaylistModel.hpp"
#include "LibraryModel.hpp"

namespace UDJ{

ActivePlaylistView::ActivePlaylistView(DataStore* dataStore, LibraryModel *libraryModel, QWidget* parent):
  QTableView(parent),
  dataStore(dataStore),
  libraryModel(libraryModel)
{
  playlistModel = new ActivePlaylistModel(dataStore, this);
  horizontalHeader()->setStretchLastSection(true);
  setItemDelegateForColumn(6, new ActivePlaylistDelegate(this));
  setModel(playlistModel);
  setSelectionBehavior(QAbstractItemView::SelectRows);
}
  
QString ActivePlaylistView::getFilePath(const QModelIndex& songIndex) const{
  return playlistModel->getFilePath(songIndex);
}

void ActivePlaylistView::addSongToPlaylist(const QModelIndex& libraryIndex){
  library_song_id_t libraryId = libraryModel->data(
    libraryIndex.sibling(libraryIndex.row(),0)).value<library_song_id_t>();
	if(! playlistModel->addSongToPlaylist(libraryId)){
		//TODO display error message
	}
}

void ActivePlaylistView::removeSong(const QModelIndex& index){
	if(! playlistModel->removeSongFromPlaylist(index)){
		//TODO display error message
	}
}

bool ActivePlaylistView::isVotesColumn(int columnIndex){
  return columnIndex == 3; 
}


} //end namespace

