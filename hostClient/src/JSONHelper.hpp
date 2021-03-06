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
#ifndef JSON_HELPER_HPP
#define JSON_HELPER_HPP
#include "ConfigDefs.hpp"
#include <vector>

class QNetworkReply;

namespace UDJ{

typedef struct {
  library_song_id_t id;
  QString songName;
  QString artistName;
  QString albumName;
  int duration;
} lib_song_t;


class JSONHelper{

public:

  static const QByteArray getJSONForLibAdd(const lib_song_t &song);

  static const QByteArray getJSONForLibAdd(
    const lib_song_t &song,
    bool &success);

  static const QByteArray getJSONForLibAdd(
    const std::vector<lib_song_t> &songs);

  static const QByteArray getJSONForLibAdd(
    const std::vector<lib_song_t>& songs,
    bool &success);

  static const std::vector<library_song_id_t>
    getUpdatedLibIds(QNetworkReply *reply);

};


} //end namespace UDJ
#endif //JSON_HELPER_HPP
